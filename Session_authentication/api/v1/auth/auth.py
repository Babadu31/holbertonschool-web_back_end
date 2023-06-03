#!/usr/bin/env python3
"""Class to manage API authentication"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class used for basic authentication
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """validates all requests to secure the API.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User object
        """
        return None

    def session_cookie(self, request=None):
        """
        Retrieve the value of the session cookie from a request.
        Args:
            request: The request object containing cookies.
        Returns:
            str: The value of the session cookie, or None if
            request is None or the cookie is not found.
        """
        if request is None:
            return None

        session_name = os.environ.get('SESSION_NAME')
        if session_name is None:
            return None

        return request.cookies.get(session_name)
