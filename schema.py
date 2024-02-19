
from pydantic import BaseModel
from typing import List
class Queries(BaseModel):
    hash_tags:list[str]


class ResObj(BaseModel):
    query: str
    nearest_keywords: List[str]



