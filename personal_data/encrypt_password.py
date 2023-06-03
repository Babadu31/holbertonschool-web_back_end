#!/usr/bin/env python3
"Encrypting passwords"
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password, which is a byte string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function checks if a provided password matches the hashed password.
    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to verify.
    Returns:
        bool: True if password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    hashed_password = hash_password(password)
    print(is_valid(hashed_password, password))
