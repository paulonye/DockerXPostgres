from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    """The url string used below is unique to postgressql
        I had to install the psycopg2 driver which is
        the DB API that moves information between SQLAlchemy and the postgres database."""

    user=os.getenv("DBUSER")
    password=os.getenv('PASSWORD')
    host=os.getenv('HOST')
    port=5432
    database=os.getenv('DBNAME')

    return create_engine(
        url="postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

if __name__ == '__main__':
    engine = get_connection()
    print('Connection Successful')
    engine.connect().close()
