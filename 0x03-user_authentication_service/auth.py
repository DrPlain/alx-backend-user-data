#!/usr/bin/env python3
""" Function that hashes password
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Hashes a password
    Return: hashed_password bytes
    """
    encoded_password = password.encode()
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ class contructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method to register user
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except Exception as err:
            pass
        if user:
            raise ValueError(f'User {email} already exists')
        else:
            hashed_password = _hash_password(password)
            registered_user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return registered_user