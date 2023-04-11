"""
GraphQL Parser Generated AST Tree Object Example

"<Document":"definitions="[
   "<Query":"selections="[
      "<Field":"name=campaign_definition",
      "arguments="[
         "<Argument":"name=where",
         "value="{
            "campaign_name":{
               "_eq":"<Variable":"name=campaign_name>"
            },
            "account_cid":{
               "_eq":"<Variable":"name=account_cid>"
            }
         }">"
      ],
      "selections="[
         "<Field":"name=ad_group_templates",
         "arguments="[
            "<Argument":"name=order_by",
            "value="{
               "id":"asc"
            }">"
         ],
         "selections="[
            "<Field":"name=id>",
            "<Field":"name=campaign_definition",
            "selections="[
               "<Field":"name=account_cid>",
               "<Field":"name=campaign_name>"
            ]">",
            "<Field":"name=ad_groups",
            "arguments="[
               "<Argument":"name=order_by",
               "value="{
                  "ad_group_index":"asc"
               }">"
            ],
            "selections="[
               "<Field":"name=adwords_id>",
               "<Field":"name=ad_group_index>"
            ]">",
            "<Field":"name=taxonomy_id>",
            "<Field":"name=targeting_set>"
         ]">",
         "<Field":"name=campaign_name>",
         "<Field":"name=id>",
         "<Field":"name=target_location>",
         "<Field":"name=adwords_id>"
      ]">"
   ],
   "name=GetAdgroupTemplates",
   "variable_definitions="[
      "<VariableDefinition":"name=campaign_name",
      "type=<NonNullType":"type=<NamedType":"name=String>>>",
      "<VariableDefinition":"name=account_cid",
      "type=<NamedType":"name=String>>"
   ]">"
]">"
"""

"""
 Mocking a gql query
 query_schema = {
    query_name(where: {field_where: {_eq: $variable_field }}) {
         field1
         field2 {
             field3
             field4
         }
    }
 }

 Root Query Mocking
 {
    'rootFieldName': 'query_name',
    'rootFields': [
       'field1',
       'field2'
    ],
    'arguments': [
        Argument(name='where', value={
            'field_where': {
                '_eq': Variable(name='variable_field')
            }
        })
    ]
    'children': [
        'query_name.field2'
    ],
 }

 Nested Field Schema
 {
    'query_name.field2': {
        'rootFieldName': 'field2',
        'rootFields': [
         'field3',
         'field4'
        ]
    }
 }
"""


def get_gql_definition_base_fields(parsed_gql):
    """Get base fields for document root

    Returns:
    Args:
        parsed_gql: GQL Document

        array of fields
    """
    fields = parsed_gql.definitions[0].selection_set.selections
    fields_array = []
    for field in fields:
        fields_array.append(field.name.value)
    return fields_array


def get_gql_selections(definition):
    """Get base fields

    Args:
        definition:

    Returns:
        array of fields
    """
    return definition.selections


def get_gql_definition_query_ast(parsed_gql):
    """Get GQL Root Query Tree

    Args:
        parsed_gql: GQL Document

    Returns:
        array of fields
    """
    return parsed_gql.definitions[0].selections[0]


def get_gql_definition_root_query_name(parsed_gql):
    """Get GQL root query name

    Args:
        parsed_gql: GQL Document

    Returns:
        :name str
    """
    return parsed_gql.definitions[0].name.value


def get_gql_definition_arguments(parsed_gql):
    """Get GQL Arguments

    Args:
        parsed_gql: GQL Document

    Returns:
        document arguments as array
    """
    return parsed_gql.definitions[0].selection_set.selections[0].arguments


def get_gql_arguments(parsed_gql):
    """Get GQL Arguments

    Args:
        parsed_gql: GQL Document

    Returns:
        document arguments as array
    """
    if hasattr(parsed_gql, "arguments"):
        return parsed_gql.arguments
    return None


def get_gql_base_fields(parsed_gql):
    """Get base fields

    Args:
        parsed_gql: GQL Document

    Returns:
        array of fields
    """
    fields_array = []
    fields = parsed_gql.selection_set.selections
    for field in fields:
        fields_array.append(field.name)
    return fields_array


def get_gql_root_name(parsed_gql):
    """Get GQL root query name

    Args:
        parsed_gql: GQL Document

    Returns:
        :name str
    """
    return parsed_gql.name


def find_ast_recursive(field_name, ast):
    """Recursively traverse and find the nested GQL Schema

    Args:
        field_name: str
        ast: GQL Document

    Returns:
        nested child GQL Document
    """
    if ast.name is not None and ast.name == field_name:
        return ast
    temp_ast = ast.selections
    final_ast = None
    for _ast in temp_ast:
        if _ast.selections is not None and len(_ast.selections) >= 1:
            final_ast = find_ast_recursive(field_name, _ast)
            if final_ast is not None:
                break
    return final_ast


def get_gql_definitions_nested_fields_ast(field_name, parsed_gql):
    """Get GQL Nested Fields Schema

    Args:
        field_name: str
        parsed_gql: GQL Document

    Returns:
        nested field schema
    """
    keys = field_name.split(".")
    query_ast = get_gql_definition_query_ast(parsed_gql)
    for key in keys:
        query_ast = find_ast_recursive(key, query_ast)
    return query_ast
