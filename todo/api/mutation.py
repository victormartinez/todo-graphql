import graphene


class Mutation(graphene.ObjectType):
    node = graphene.relay.Node.Field()
