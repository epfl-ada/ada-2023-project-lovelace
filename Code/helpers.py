import numpy as np
import pandas as pd
import ast


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