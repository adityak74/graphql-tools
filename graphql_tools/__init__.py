"""GraphQL Tools init"""
import logging
from graphql import DocumentNode
from graphql.graphql import parse
from graphql_tools.lib.gql_helpers import (
    get_gql_definition_root_query_name,
    get_gql_definition_arguments,
    get_gql_definition_base_fields,
)
from graphql_tools.models.graphql_mock_schema import GQLMockQuerySchema


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def parse_gql_query(query: str) -> DocumentNode:
    """Parse GQL Query"""
    parsed_query = parse(query, no_location=True)
    return parsed_query


def generate_gql_mock(parsed_query: DocumentNode):
    """Generate GQL mock from parsed query DocumentNode"""
    root_query_name = get_gql_definition_root_query_name(parsed_query)
    arguments = get_gql_definition_arguments(parsed_query)
    root_fields = get_gql_definition_base_fields(parsed_query)
    _mocked_gql_obj = GQLMockQuerySchema(
        rootFieldName=root_query_name,
        rootFields=root_fields,
        arguments=arguments if len(arguments) else None,
    )
    return _mocked_gql_obj
