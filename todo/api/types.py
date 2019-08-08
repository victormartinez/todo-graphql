import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType

from todo.api.models import Task as TaskModel


class Task(SQLAlchemyObjectType):

    class Meta:
        model = TaskModel
        interfaces = (graphene.relay.Node, )
