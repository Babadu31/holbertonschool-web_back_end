#!/usr/bin/env python3

"""
filtered_logger.py
Ce module fournit une classe RedactingFormatter
pour utilisation avec le module de logging intégré de Python.
Cette classe est utilisée pour masquer les informations sensibles,
spécifiées par les noms de champs, dans les messages de log.

Le module contient également une fonction utilitaire `filter_datum`
pour remplacer les informations sensibles dans les chaînes de texte.
Il contient aussi une fonction `get_logger`
pour créer un logger avec un RedactingFormatter en tant que formateur.

Enfin, il définit une constante PII_FIELDS qui contient les
champs considérés comme des Informations Personnellement Identifiables (PII).
"""


import os
import re
import logging
import mysql.connector
from typing import List

# Define fields considered as PII (Personally Identifiable Information)
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for logging which redacts sensitive information
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Overrides logging.Formatter format method to include PII filtering
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Returns a logger object
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the database
    """

    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
