"""GraphQL Tools init"""
import logging
from graphql import GraphQLSchema, DocumentNode
from graphql.graphql import parse

from lib.func_tools import function_will_exit_failure
from lib.gql_helpers import (
    get_gql_definition_root_query_name,
    get_gql_definition_arguments,
    get_gql_definition_base_fields,
)
from models.graphql_mock_schema import GQLMockQuerySchema


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def mock_gql_schema(schema: GraphQLSchema):
    """Mocks given GQL Schema"""
    if schema is None:
        function_will_exit_failure("Invalid GQL schema", logger)
    if isinstance(schema, GraphQLSchema):
        function_will_exit_failure("GQL schema is not of type GraphQLSchema", logger)


def parse_gql_query(query: str) -> DocumentNode:
    """Parse GQL Query"""
    parsed_query = parse(query)
    return parsed_query


def generate_gql_mock(parsed_query: DocumentNode):
    """Generate GQL mock from parsed query DocumentNode"""
    root_query_name = get_gql_definition_root_query_name(parsed_query)
    arguments = get_gql_definition_arguments(parsed_query)
    root_fields = get_gql_definition_base_fields(parsed_query)
    _mocked_gql_obj = GQLMockQuerySchema(
        rootFieldName=root_query_name,
        rootFields=root_fields,
        arguments=arguments if len(arguments) > 0 else None,
    )
    return _mocked_gql_obj
