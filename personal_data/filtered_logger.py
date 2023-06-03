#!/usr/bin/env python3
import re
import logging
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = ("[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: "
              "%(message)s")
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        original_format = super().format(record)
        return self.filter_datum(
            self.fields, self.REDACTION, original_format, self.SEPARATOR)

    @staticmethod
    def filter_datum(fields: List[str], redaction: str, message: str,
                     separator: str) -> str:
        """ filter out specific fields in datum """
        for field in fields:
            message = re.sub(f"{field}=[^;]+", f"{field}={redaction}", message)
        return message
