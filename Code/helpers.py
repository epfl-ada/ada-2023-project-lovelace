import numpy as np
import pandas as pd
import ast
import unicodedata
import re


def parse_list(string):
    """
    Parse a string representation of a list, safely evaluating it back into a list.

    Parameters:
    string (str): The string representation of a list.

    Returns:
    list: The list evaluated from the string, or np.nan if evaluation fails.
    """
    try:
        return ast.literal_eval(string)
    except:
        return np.nan


def parse_dict(string):
    """
    Parse a string representation of a dictionary and extract its values into a list.

    Parameters:
    string (str): The string representation of a dictionary.

    Returns:
    list: A list of values from the dictionary, or np.nan if evaluation fails or if the dictionary is empty.
    """
    try:
        genres_dict = ast.literal_eval(string)
        values = list(genres_dict.values())
        return values if values else np.nan
    except:
        return np.nan


def standardize_str(string):
    """
    Standardize a string by removing accents and special characters, converting to lowercase, and removing extra spaces.

    Parameters:
    string (str): The string to standardize.

    Returns:
    str: The standardized string.
    """
    # normalize the string to unicode NFKD format and convert to lowercase
    nfkd_form = unicodedata.normalize('NFKD', string).lower()
    # remove non-alphanumeric characters (excluding spaces)
    no_special_chars = re.sub('[^a-z0-9 ]', '', nfkd_form)
    # replace multiple spaces with a single space
    single_spaced = re.sub('\s+', ' ', no_special_chars)
    # strip leading and trailing spaces
    stripped = single_spaced.strip()

    return stripped
