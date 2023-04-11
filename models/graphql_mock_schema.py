"""GQL Mock schema model"""
from pydantic import BaseModel as PydanticBaseModel
from typing import List, Optional

from graphql import GraphQLArgument


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class GQLMockQuerySchema(BaseModel):
    """GQL Mock Query Schema class"""

    rootFieldName: Optional[str]
    rootFields: List[str]
    arguments: Optional[List[GraphQLArgument]]
    children: Optional[List[str]]
