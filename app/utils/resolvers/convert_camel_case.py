"""
This module contains function to convert to camel case
"""
import re


def convert_camel_case(name: str) -> str:
    """
    This function is converting name to camel case
    :param name: str with column name
    :return: column name in camel case
    """
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    name = pattern.sub("_", name).lower()
    return name
