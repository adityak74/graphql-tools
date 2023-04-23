"""GQL Mock Schema Types"""
from lib.utilities import get_gql_type_node_from_value
from graphql import NameNode, VariableNode, ArgumentNode
from graphql_tools.exceptions import GQLInvalidTypeException


class GQLMockArgument:
    """GQL Mock Argument type"""

    def __init__(self, name, variable_name=None, value=None):
        """set the mock argument and return GQLArgument Node"""
        if not isinstance(name, str):
            raise GQLInvalidTypeException("Name is not a string")
        self.name_node = NameNode(value=name)
        self.value_node = None
        if variable_name:
            self.value_node = VariableNode(name=NameNode(value=variable_name))
        elif value:
            python_type, gql_value_node_type = get_gql_type_node_from_value(value)
            self.value_node = gql_value_node_type(value=str(value))

    def to_gql(self) -> ArgumentNode:
        """Return GQL argument node"""
        return ArgumentNode(name=self.name_node, value=self.value_node)
