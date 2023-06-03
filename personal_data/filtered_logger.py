#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub('|'.join(f'{field}=.*?{separator}' for field in fields), f'{redaction}{separator}', message)
