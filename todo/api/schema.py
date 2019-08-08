import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from todo.api.types import Task


class Query(graphene.ObjectType):
    hello = graphene.String(description="A typical hello world")
    tasks = SQLAlchemyConnectionField(Task)

    def resolve_hello(self, info):
        return "World"


schema = graphene.Schema(query=Query)
