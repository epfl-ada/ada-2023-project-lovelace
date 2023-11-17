import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast
import unicodedata
import re
import networkx as nx
from rapidfuzz import process


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
        string = string.replace("\n", "")
        string = string.replace("'", "")
        string = string[1:-1]
        return np.array(string.split(" "))
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


def get_best_match(row, grouped_df, scorer, threshold=95):
    """
       Find the best match with a given minimum similarity threshold for a given movie title.

       Parameters:
       row (Series): The row containing the movie information.
       grouped_df (DataFrameGroupBy): The grouped DataFrame containing movies by release year.
       scorer: The scoring function for similarity comparison.
       threshold (int): The minimum similarity threshold for considering a match.

       Returns:
       The best matching movie title if its similarity is above the threshold, otherwise np.nan.
       """
    # filter the imdb dataframe to check only for movies with the same release year
    same_year_movies = grouped_df.get_group(row['releaseYear'])['movieNameStd'] if \
        (row['releaseYear'] in grouped_df.groups) else []
    # find the best match for the given movie title
    best_match = process.extractOne(row['movieNameStd'], same_year_movies, scorer=scorer)
    # return the best match if its similarity is above the threshold
    return best_match[0] if best_match and best_match[1] >= threshold else np.nan


def plot_degree_distribution(G):
    """
    Plots the degree distribution of a graph.

    This function calculates the degree of each node in the graph G. It then aggregates
    and plots the frequency of each degree in the graph, displaying the result as a bar chart.
    The x-axis of the chart represents the degree of the nodes, and the y-axis shows the
    frequency of each degree in the graph.

    Parameters:
    G (networkx.Graph): A networkx graph object whose degree distribution is to be plotted.
    """
    degrees = {}
    for node in G.nodes():
        degree = G.degree(node)
        if degree not in degrees:
            degrees[degree] = 0
        degrees[degree] += 1
    sorted_degree = sorted(degrees.items())
    deg = [k for (k, v) in sorted_degree]
    cnt = [v for (k, v) in sorted_degree]
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.bar(deg, cnt, width=0.80, color='b')
    plt.title("Degree Distribution")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.05 for d in deg])
    ax.set_xticklabels(deg)
    plt.show()


def describe_graph(G):
    """
    Prints various properties of the given graph.

    This function takes a graph G and prints its properties, including whether the
    graph is connected, the average shortest path length, the diameter of the graph,
    its sparsity, and the global clustering coefficient (transitivity).

    Parameters:
    G (networkx.Graph): A networkx graph object whose properties are to be described.
    """
    print(G)
    if nx.is_connected(G):
        print("Avg. Shortest Path Length: %.4f" % nx.average_shortest_path_length(G))
        print("Diameter: %.4f" % nx.diameter(G))  # Longest shortest path
    else:
        print("Graph is not connected")
        print("Diameter and Avg shortest path length are not defined!")
    print("Sparsity: %.4f" % nx.density(G))  # #edges/#edges-complete-graph
    print("Global clustering coefficient aka Transitivity: %.4f" % nx.transitivity(G))


def visualize_graph(G, with_labels=True, k=None, alpha=1.0, node_shape='o'):
    """
    Visualizes the given graph using NetworkX's drawing methods.

    This function takes a graph G and plots it using a spring layout. The visualization
    includes options to display node labels, adjust the transparency of edges, and
    specify the shape of the nodes. The function is primarily used for a quick and easy
    visual representation of the graph structure.

    Parameters:
    G (networkx.Graph): A networkx graph object to be visualized.
    with_labels (bool): If True, the nodes are labeled with their ids.
    k (float): Optimal distance between nodes. If None, the value is chosen automatically.
    alpha (float): Transparency of the edges.
    node_shape (str): Shape of the nodes.
    """
    pos = nx.spring_layout(G, k=k)
    if with_labels:
        nx.draw_networkx_labels(G, pos, labels=dict([(n, n) for n in G.nodes()]))
    nx.draw_networkx_edges(G, pos, alpha=alpha)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), node_color='g', node_shape=node_shape)
    plt.axis('off')
    plt.show()
