from sqlalchemy import create_engine, pool


def get_engine(db_url):
    engine = create_engine(
        db_url,
        connect_args={"connect_timeout": 5},
    )
    return engine


def get_engine_url(engine):
    return engine.url
