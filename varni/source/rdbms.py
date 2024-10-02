from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from source import MasterSource

class SQLAlchemySource(MasterSource):
    def __init__(self, user, master_permissions, model, database_url):
        """
        Initialize SQLAlchemySource with the model, user, and database session.
        """
        super().__init__(user, master_permissions)
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.model = model

    @MasterSource.permission_required("select")
    def select(self, entity_name, columns, joins=None, filters=None):
        """
        Select the allowed columns for the specified entity with optional filters and joins.
        
        :param entity_name: The name of the entity being queried (e.g., "User").
        :param columns: List of columns to select.
        :param joins: List of relationships to join (foreign key relationships).
        :param filters: Dictionary of filters to apply to the query.
        """
        query = self.session.query(*[getattr(self.model, col) for col in columns])

        # Handle joins (foreign key relationships)
        if joins:
            for relationship in joins:
                query = query.options(joinedload(relationship))

        # Apply any filters provided
        if filters:
            query = query.filter_by(**filters)
        
        return query.all()

    @MasterSource.permission_required("write")
    def insert(self, entity_name, columns, **data):
        """
        Insert data into the specified entity if permission allows.
        """
        obj = self.model(**{key: value for key, value in data.items() if key in columns})
        self.session.add(obj)
        self.session.commit()
        return obj

    @MasterSource.permission_required("write")
    def update(self, entity_name, columns, filter_by, update_data):
        """
        Update data in the specified entity if permission allows.
        """
        obj = self.session.query(self.model).filter_by(**filter_by).first()
        if obj:
            for key, value in update_data.items():
                if key in columns:  # Ensure permission to update this column
                    setattr(obj, key, value)
            self.session.commit()
        return obj

    @MasterSource.permission_required("write")
    def delete(self, entity_name, columns, **filter_by):
        """
        Delete data from the specified entity if permission allows.
        """
        obj = self.session.query(self.model).filter_by(**filter_by).first()
        if obj:
            self.session.delete(obj)
            self.session.commit()
