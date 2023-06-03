#!/usr/bin/env python3
"""Basic Authentication"""

from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from typing import TypeVar, List
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""
    def __init__(self):
        """Constructor"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base64 authorization header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """Decode base64 authorization header"""

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_header = b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decoded_header.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """User object from credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        for u in user:
            if u.is_valid_password(user_pwd):
                return u
        return None
