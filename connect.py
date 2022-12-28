from sqlalchemy import create_engine, text
import os

# database credentials
lis = []
with open('credentials.txt', 'r') as file:
    for line in file:
        lis.append(line.strip())

user = lis[0]
password = lis[1]
#host = '10.64.16.3'
host = str(lis[2])
port = 5432
database = lis[3]

def get_connection():
    """The url string used below is unique to mysql
        I had to install the pymysql driver which is
        the DB API that moves information between SQLAlchemy and the mysql database."""

    return create_engine(
        url="postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

if __name__ == '__main__':
    engine = get_connection()
    print('Connection Successful')
    engine.connect().close()
