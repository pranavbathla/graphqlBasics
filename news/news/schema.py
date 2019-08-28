import graphene
import reporting.schema

class Query(reporting.schema.Query, graphene.ObjectType):
    pass


class Mutation(reporting.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
