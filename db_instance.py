import flask_sqlalchemy

class Db:
    INSTANCE = None
    @staticmethod
    def get_instance(__self__ ):
        if __self__.INSTANCE is None:
            __self__.INSTANCE = flask_sqlalchemy.SQLAlchemy()
        return __self__.INSTANCE
