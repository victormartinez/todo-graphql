import graphene

from todo.api.query import Query
from todo.api.mutation import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
