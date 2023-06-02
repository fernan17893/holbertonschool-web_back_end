#!/usr/bin/env python3
"""Auth class"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""


    def __init__(self):
        """Constructor"""


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires authorization method"""
        return False
    
    def authorization_header(sefl, request=None) -> str:
        """Authorization header method"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None