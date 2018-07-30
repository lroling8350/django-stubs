# Stubs for django.contrib.sessions.backends.cache (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.sessions.backends.base import SessionBase
from typing import Any, Optional

from typing import Any, Dict, Optional

KEY_PREFIX: str

class SessionStore(SessionBase):
    cache_key_prefix: Any = ...
    _cache: Any = ...
    def __init__(self, session_key: None = ...) -> None: ...
    @property
    def cache_key(self) -> str: ...
    _session_key: Any = ...
    def load(self) -> Dict[Any, Any]: ...
    modified: bool = ...
    def create(self) -> None: ...
    def save(self, must_create: bool = ...) -> None: ...
    def exists(self, session_key: Optional[str]) -> bool: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    @classmethod
    def clear_expired(cls) -> None: ...