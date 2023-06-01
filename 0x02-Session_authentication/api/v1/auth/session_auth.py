#!/usr/bin/env python3
from uuid import uuid4
from api.v1.auth.auth import Auth
""" Module for SessionAuth class
"""


class SessionAuth(Auth):
    """ class SessionAuth for session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a user_id
        """
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
