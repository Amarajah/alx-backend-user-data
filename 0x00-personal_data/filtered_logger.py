#!/usr/bin/env python3
"""0. Regex-ing"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function called filter_datum that returns the log message obfuscated"""
    regex_pattern = f'({re.escape(separator.join(fields))})'
    return re.sub(regex_pattern, redaction, message)
