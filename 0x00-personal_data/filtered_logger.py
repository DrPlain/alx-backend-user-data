#!/usr/bin/env python3
""" Obfuscates user's personal data """
from typing import List
import logging
import re

PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'ip')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Obfuscates user's personal data """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """ Returns a custom logger """

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        filtered_record = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.msg = filtered_record
        return super(RedactingFormatter, self).format(record)
