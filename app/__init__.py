from bottle import Bottle, TEMPLATE_PATH
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)

app = Bottle()
TEMPLATE_PATH.insert(0, 'app/views/')
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

app.install(plugin)

from app.controllers import default
from app.models import tables
