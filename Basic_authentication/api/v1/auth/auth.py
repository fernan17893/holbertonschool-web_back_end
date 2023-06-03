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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False
        return True
        

    def authorization_header(sefl, request=None) -> str:
        """Authorization header method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None
