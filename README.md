# GraphQL Tools Python

This library provides interface for GQL Schema mocking and validating functionality. Validating GraphQL queries for
their correct schema is essential for synchronous development of GQL backend and front end.

### Usage

To use this library simply import the `GQLMockSchemaQuery` class. Let's mock this example query below:

```
HELLO_QUERY = """
query GetHelloQuery {
    hello
}
"""
```

#### Code

```
from graphql_tools import GQLMockQuerySchema, parse_gql_query, generate_gql_mock

parsed_query = parse_gql_query(query=HELLO_QUERY)
gql_mock_schema = GQLMockQuerySchema(
	rootFieldName="GetHelloQuery",
	rootFields=["hello"],
)
gql_generated_mock = generate_gql_mock(parsed_query)
assert gql_generated_mock == gql_mock_schema
```

1. `parse_gql_query` parses the given Query and returns the AST.
2. `GQLMockQuerySchema` takes `rootFieldName` which is the query name. `rootFields` are the fields that we are querying for.
3. `generate_gql_mock` generates the mock object for the parsed query.
4. `gql_generated_mock` can be asserted to match with our mocked query schema validates that the our expected query
is correctly shaped.

### Advantages

Client applications that use the GQL queries to query other services tend to modify queries. Unexpected query fields
or shape of the query can break the applications. Validating by Mocking the Query Schema would enforce query shapes
and keeping the application intact.

Using this a part of your testing suite by writing validating tests allows the developer to modify the query but also
enforce to modify the following code logic if there has been changes to the query.
