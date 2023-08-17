#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


def _hash_password(password: str) -> bytes:
    """method that takes in a password string
    arguments and returns bytes."""
    passwrd = password.encode('utf-8')
    return bcrypt.hashpw(passwrd, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """If a user already exist with the passed email,
        raise a ValueError with the message
        User <user's email> already exists.
        If not, hash the password with _hash_password,
        save the user to the database
        using self._db and return the User object.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            usr = self._db.add_user(email, hashed)
            return usr
        raise ValueError(f"User {email} already exists")
