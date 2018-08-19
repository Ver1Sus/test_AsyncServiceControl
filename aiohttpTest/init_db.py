from sqlalchemy import create_engine, MetaData

from settings import config
from db import flagStatus


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"



if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    #create_tables(engine)
    #sample_data(engine)