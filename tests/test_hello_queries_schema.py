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
from graphql_tools.types import GQLMockArgument
from graphql_tools.exceptions import GQLInvalidTypeException

HELLO_QUERY = """
query GetHelloQuery {
    hello
}
"""

HELLO_QUERY_ARGS = """
query GetHelloQueryWithArgs($hello: String) {
    hello(world: $hello) {
        name
    }
}
"""

HELLO_QUERY_INT_VALUE = """
query GetHelloQueryWithInt {
    hello(world: 1) {
        name
    }
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


def test_gql_schema_validation_with_args():
    """Test GQL Schema Validation"""
    parsed_query = parse_gql_query(query=HELLO_QUERY_ARGS)
    assert isinstance(parsed_query, DocumentNode) is True
    gql_mock_schema = GQLMockQuerySchema(
        rootFieldName="GetHelloQueryWithArgs",
        rootFields=["hello"],
        arguments=(GQLMockArgument(name="world", variable_name="hello").to_gql(),),
    )
    gql_generated_mock = generate_gql_mock(parsed_query)
    assert gql_generated_mock.rootFieldName == gql_mock_schema.rootFieldName
    assert gql_generated_mock.rootFields == gql_mock_schema.rootFields
    assert gql_generated_mock.arguments == gql_mock_schema.arguments


def test_gql_schema_validation_fail_syntax_error():
    """Test GQL Schema Validation Fail Syntax Error"""
    with pytest.raises(GraphQLSyntaxError):
        parse_gql_query(query=HELLO_QUERY_SYNTAX_ERROR)


def test_gql_schema_validation_with_args_int():
    """Test GQL Schema Validation with args for int"""
    parsed_query = parse_gql_query(query=HELLO_QUERY_INT_VALUE)
    assert isinstance(parsed_query, DocumentNode) is True
    gql_mock_schema = GQLMockQuerySchema(
        rootFieldName="GetHelloQueryWithInt",
        rootFields=["hello"],
        arguments=(GQLMockArgument(name="world", value=1).to_gql(),),
    )
    gql_generated_mock = generate_gql_mock(parsed_query)
    assert gql_generated_mock.rootFieldName == gql_mock_schema.rootFieldName
    assert gql_generated_mock.rootFields == gql_mock_schema.rootFields
    assert gql_generated_mock.arguments == gql_mock_schema.arguments


def test_gql_mock_argument_name_type_fail():
    """Test GQL Mock argument for name type fail"""
    with pytest.raises(GQLInvalidTypeException):
        GQLMockArgument(name=None).to_gql()


def test_gql_schema_validation_with_args_int_benchmark(benchmark):
    parsed_query = parse_gql_query(query=HELLO_QUERY_INT_VALUE)
    """Test GQL Schema Validation with args for int benchmark"""
    benchmark(generate_gql_mock, parsed_query)
