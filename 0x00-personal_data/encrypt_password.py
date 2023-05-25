#!/usr/bin/env python3
""" Password encrytpion """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes in a password string and returns a
    hashed password
    Args:
        password: Byte string
    """
    encoded_password = password.encode()
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())
