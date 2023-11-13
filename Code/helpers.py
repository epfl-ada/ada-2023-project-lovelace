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
    Parse a string representation of a dictionary safely evaluating it back into a dictionary.

    Parameters:
    string (str): The string representation of a dictionary.

    Returns:
    dict: The dict evaluated from the string, or np.nan if evaluation fails.
    """
    try:
        return ast.literal_eval(string)
    except:
        return np.nan


def parse_dict_to_list(string):
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


def keep_as_dict(keys, values):
    """
    Create a dictionary from the given keys and values, filtering out entries where values are NaN.

    Parameters:
    - keys (list): List of keys for the dictionary.
    - values (list): List of values for the dictionary.

    Returns:
    - dict or np.nan: A dictionary created from the provided keys and values, or np.nan if no valid entries are present.
    """
    d = dict(zip(keys, values))
    d = {k: v for (k, v) in d.items() if v == v}  # Filtering out NaN values
    return d if len(d) else np.nan


def explode_on_movies(df):
    """
    Explodes the provided DataFrame on the 'fbID' column and extracts information from columns in a dictionary format.

    Parameters:
    - df (pandas.DataFrame): Input DataFrame containing information about movies.

    Returns:
    - pandas.DataFrame: Exploded DataFrame with expanded rows and extracted information from specified columns.
    """
    explode_columns = ["ageAtMovieRelease", "category", "winner"]
    df = df.explode("fbID")

    for col in explode_columns:
        df[col] = df.apply(
            lambda row: row[col].get(row["fbID"])
            if isinstance(row[col], dict)
            else np.nan,
            axis=1,
        )
    return df


def actors_agg(df):
    """
    Aggregates information about actors from the provided DataFrame.

    Parameters:
    - df (pandas.DataFrame): Input DataFrame containing information about actors.

    Returns:
    - pandas.Series: Aggregated Series with information about actors, including 'fbID', 'ageAtMovieRelease', 'category', and 'winner'.
    """
    fbID = np.unique(df["fbID"])
    return pd.Series(
        {
            "fbID": fbID,
            "ageAtMovieRelease": keep_as_dict(fbID, df["ageAtMovieRelease"]),
            "category": keep_as_dict(fbID, df["category"]),
            "winner": keep_as_dict(fbID, df["winner"]),
        }
    )


def parse_list_actors(string):
    """
    Parse a string representation of a list, safely evaluating it back into a list.

    Parameters:
    string (str): The string representation of a list.

    Returns:
    list: The list evaluated from the string, or np.nan if evaluation fails.
    """
    try:
        return string.split(",")
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
    nfkd_form = unicodedata.normalize("NFKD", string).lower()
    # remove non-alphanumeric characters (excluding spaces)
    no_special_chars = re.sub("[^a-z0-9 ]", "", nfkd_form)
    # replace multiple spaces with a single space
    single_spaced = re.sub("\s+", " ", no_special_chars)
    # strip leading and trailing spaces
    stripped = single_spaced.strip()

    return stripped
