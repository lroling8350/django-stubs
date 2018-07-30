# Stubs for django.templatetags.cache (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.template import Node
from typing import Any

from django.template.base import FilterExpression, NodeList, Parser, Token
from django.template.context import Context
from django.utils.safestring import SafeText
from typing import List

register: Any

class CacheNode(Node):
    nodelist: Any = ...
    expire_time_var: Any = ...
    fragment_name: Any = ...
    vary_on: Any = ...
    cache_name: Any = ...
    def __init__(
        self,
        nodelist: NodeList,
        expire_time_var: FilterExpression,
        fragment_name: str,
        vary_on: List[FilterExpression],
        cache_name: None,
    ) -> None: ...
    def render(self, context: Context) -> SafeText: ...

def do_cache(parser: Parser, token: Token) -> CacheNode: ...