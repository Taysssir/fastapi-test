import databases
import sqlalchemy
from functools import lru_cache
from api import config
from api.models import metadata

# Using Pydantic to load configuration
@lru_cache()
def setting():
    return config.Settings()

def database_pgsql_url_config():
    # Connect To Local DB 
    # return str(setting().DB_CONNECTION + "://" + setting().DB_USERNAME + ":" + setting().DB_PASSWORD +
    #            "@" + setting().DB_HOST + ":" + setting().DB_PORT + "/" + setting().DB_DATABASE)
    # Connect To DB_CONTAINER
    return str(setting().DB_CONNECTION + "://" + setting().DB_USERNAME + ":" + setting().DB_PASSWORD +
               "@" + setting().DB_CONTAINER  + "/" + setting().DB_DATABASE)

database = databases.Database(database_pgsql_url_config())
engine = sqlalchemy.create_engine(database_pgsql_url_config())
metadata.create_all(engine)
