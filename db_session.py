# db_session.py
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

SqlAlchemyBase = declarative_base()

__factory = None


def global_init(db_file):
    global __factory
    if __factory:
        return

    engine = sa.create_engine(f"sqlite:///{db_file}", echo=False)
    __factory = sessionmaker(bind=engine)

    from models import __all_models  # noqa

    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()
