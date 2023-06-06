#!/usr/bin/env python
""" Function that hashes password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a password
    Return: hashed_password bytes
    """
    encoded_password = password.encode()
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())
