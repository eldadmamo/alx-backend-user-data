#!/usr/bin/env python3
"""
Encrypting valid password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting password and returns salted hash"""
    # Generate a random salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check password hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
