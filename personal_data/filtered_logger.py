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


import re
import logging
from typing import List

# Champs à considérer comme PII
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """
    Classe RedactingFormatter
    Elle étend la classe Formatter du module logging
    pour ajouter la fonctionnalité de masquage des PII.
    """

    REDACTION = "***"
    FORMAT = ("[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: "
              "%(message)s")
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filtre les valeurs dans les enregistrements
        de log entrants en utilisant filter_datum"""
        original_format = super().format(record)
        return self.filter_datum(
            self.fields, self.REDACTION, original_format, self.SEPARATOR)

    @staticmethod
    def filter_datum(fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """
        Filtre des champs spécifiques dans le datum
        """
        for field in fields:
            message = re.sub(f"{field}=[^;]+", f"{field}={redaction}", message)
        return message


def get_logger() -> logging.Logger:
    """
    Renvoie un objet logging.Logger
    Le logger a pour nom "user_data", son niveau est réglé sur INFO,
    il n'envoie pas de messages à d'autres loggers et
    utilise un StreamHandler avec RedactingFormatter comme formateur.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger
