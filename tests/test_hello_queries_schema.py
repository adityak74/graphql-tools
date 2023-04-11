"""Test Hello Query Schema"""
import pytest
from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLSyntaxError,
    DocumentNode,
)
from graphql_tools import GQLMockQuerySchema, parse_gql_query, generate_gql_mock


HELLO_QUERY = """
query GetHelloQuery {
    hello
}
"""

HELLO_QUERY_SYNTAX_ERROR = HELLO_QUERY + "+"


async def resolve_hello(obj, info):
    return "world"


schema = GraphQLSchema(
    query=GraphQLObjectType(
        name="RootQueryType",
        fields={"hello": GraphQLField(GraphQLString, resolve=resolve_hello)},
    )
)


def test_gql_schema_validation():
    """Test GQL Schema Validation"""
    parsed_query = parse_gql_query(query=HELLO_QUERY)
    assert isinstance(parsed_query, DocumentNode) is True
    gql_mock_schema = GQLMockQuerySchema(
        rootFieldName="GetHelloQuery",
        rootFields=["hello"],
    )
    gql_generated_mock = generate_gql_mock(parsed_query)
    assert gql_generated_mock == gql_mock_schema


def test_gql_schema_validation_fail_syntax_error():
    """Test GQL Schema Validation fail syntax error"""
    with pytest.raises(GraphQLSyntaxError):
        parse_gql_query(query=HELLO_QUERY_SYNTAX_ERROR)
