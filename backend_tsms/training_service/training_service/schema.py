import graphene
from graphene_django import DjangoObjectType
from graphene_federation import build_schema, extend, external,key

from endpoints.mutationQuery import Query as query_data
from endpoints.mutationQuery import Mutation as mutation_data



schema = build_schema(query=query_data,mutation=mutation_data)