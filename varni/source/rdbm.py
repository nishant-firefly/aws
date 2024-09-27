from .source import BaseSource
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class SQLAlchemyHandler(BaseSource):
    def __init__(self, model, database_url, user, permissions):
        super().__init__(user, permissions)
        self.model = model
        engine = create_engine(database_url)
        self.session = sessionmaker(bind=engine)()

    @BaseSource.permission_required("select")
    def select(self, entity_name, columns):
        # Select only the allowed columns
        query = self.session.query(*[getattr(self.model, col) for col in columns])
        return query.all()

    @BaseSource.permission_required("write")
    def create(self, entity_name, columns, **kwargs):
        # Insert new record with allowed fields
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

    @BaseSource.permission_required("read")
    def read(self, entity_name, columns, **kwargs):
        # Filter with allowed columns
        return self.session.query(self.model).filter_by(**kwargs).all()

    @BaseSource.permission_required("write")
    def update(self, entity_name, columns, filter_dict, update_dict):
        # Update only allowed fields
        obj = self.session.query(self.model).filter_by(**filter_dict).first()
        if obj:
            for key, value in update_dict.items():
                setattr(obj, key, value)
            self.session.commit()
        return obj

    @BaseSource.permission_required("write")
    def delete(self, entity_name, columns, **kwargs):
        # Delete record
        obj = self.session.query(self.model).filter_by(**kwargs).first()
        if obj:
            self.session.delete(obj)
            self.session.commit()
