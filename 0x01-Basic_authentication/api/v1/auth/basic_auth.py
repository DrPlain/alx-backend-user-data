#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts and returns base64 authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes and returns the decoded value of
        Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            # header_bytes = base64_authorization_header.encode('utf-8')
            utf8_bytes = base64.b64decode(base64_authorization_header)
            utf8_str = utf8_bytes.decode('utf-8')
            return utf8_str
        except Exception as err:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple:
        """ Extracts user's credentials and returns user
        email and password from base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':')
        return email, password