from neomodel import (
    config, StructuredNode, StructuredRel, StringProperty, UniqueIdProperty, RelationshipTo
)
import os
from dotenv import load_dotenv

load_dotenv()


config.DATABASE_URL = f'bolt://{os.environ["NEO4J_USER"]}:{os.environ["NEO4J_PASSWORD"]}@localhost:7687'  # default

class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

class Field(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    country = RelationshipTo(Country, 'IS_FROM')
    field = RelationshipTo(Field, 'WORKS_IN')


