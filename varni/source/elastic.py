from elasticsearch import Elasticsearch
from .source import BaseSource
class ElasticsearchHandler(BaseSource):
    def __init__(self, index_name, es_url, es_user, es_password, user, permissions):
        super().__init__(user, permissions)
        self.index_name = index_name
        self.es = Elasticsearch([es_url], http_auth=(es_user, es_password))

    @BaseSource.permission_required("select")
    def select(self, entity_name, columns, nested_fields=None):
        """
        Perform a select query for both top-level and nested fields.
        :param entity_name: The entity being queried
        :param columns: List of top-level fields to retrieve
        :param nested_fields: A dictionary of nested field paths and columns to retrieve
        """
        query = {
            "_source": columns,  # Main document columns
            "query": {
                "bool": {
                    "must": [
                        {"match_all": {}}
                    ]
                }
            }
        }

        # If there are nested fields, construct a nested query
        if nested_fields:
            for path, fields in nested_fields.items():
                query['query']['bool']['must'].append({
                    "nested": {
                        "path": path,
                        "query": {
                            "bool": {
                                "must": [
                                    {"exists": {"field": path}}
                                ]
                            }
                        },
                        "_source": fields
                    }
                })

        # Execute the query and return the results
        return self.es.search(index=self.index_name, body=query)

    @BaseSource.permission_required("write")
    def create(self, entity_name, columns, **kwargs):
        """
        Insert a new document with the allowed fields.
        :param entity_name: The entity being modified
        :param columns: List of top-level fields being inserted
        :param kwargs: Document data
        """
        self.es.index(index=self.index_name, body=kwargs)

    @BaseSource.permission_required("read")
    def read(self, entity_name, columns, nested_fields=None, **kwargs):
        """
        Perform a read query with both top-level and nested fields.
        :param entity_name: The entity being queried
        :param columns: List of top-level fields to retrieve
        :param nested_fields: Dictionary of nested field paths and columns
        """
        query = {
            "_source": columns,  # Top-level fields
            "query": {
                "bool": {
                    "must": [
                        {"match": kwargs}  # Filter condition for top-level fields
                    ]
                }
            }
        }

        # If there are nested fields, add them to the query
        if nested_fields:
            for path, fields in nested_fields.items():
                query['query']['bool']['must'].append({
                    "nested": {
                        "path": path,
                        "query": {
                            "bool": {
                                "must": [
                                    {"exists": {"field": path}}
                                ]
                            }
                        },
                        "_source": fields
                    }
                })

        # Execute the query and return the results
        return self.es.search(index=self.index_name, body=query)

    @BaseSource.permission_required("write")
    def update(self, entity_name, columns, doc_id, update_dict, nested_fields=None):
        """
        Update a document with both top-level and nested fields.
        :param entity_name: The entity being modified
        :param columns: Top-level fields being updated
        :param doc_id: The document ID
        :param update_dict: Data to update
        :param nested_fields: Nested fields to update
        """
        # Prepare update body with top-level fields
        update_body = {
            "doc": update_dict
        }

        # Update the document
        self.es.update(index=self.index_name, id=doc_id, body=update_body)

    @BaseSource.permission_required("write")
    def delete(self, entity_name, columns, doc_id):
        """
        Delete a document.
        :param entity_name: The entity being modified
        :param columns: Not used here (needed for permission check)
        :param doc_id: The document ID
        """
        self.es.delete(index=self.index_name, id=doc_id)
