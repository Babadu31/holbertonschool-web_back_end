#!/usr/bin/env python3
"""
Filtered logger module
"""

from typing import List
import logging
import os
import re
import mysql.connector
from mysql.connector import connection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    def __init__(self, fields: List[str]):
        """
        Constructor method
        """
        super(RedactingFormatter, self).__init__()
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using filter_datum. Values for fields
        in fields should be filtered.
        """
        return filter_datum(self.fields, "***", super().format(record), ";")


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(sh)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    Returns a connector to the database
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db
    )


def main() -> None:
    """
    Obtain a database connection using get_db and retrieve all rows in the users table
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        message = '; '.join([f'{field}={value}' for field, value in zip(cursor.column_names, row)])
        message += ';'
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
