"""Utilities"""

from graphql import IntValueNode, StringValueNode, BooleanValueNode, FloatValueNode

type_to_gql_node = {
    int: IntValueNode,
    float: FloatValueNode,
    bool: BooleanValueNode,
    str: StringValueNode,
}


def get_gql_type_node_from_value(value: any):
    """Get gql node type from given python type"""
    inferred_type = type(value)
    return (inferred_type, type_to_gql_node[inferred_type]) or None
