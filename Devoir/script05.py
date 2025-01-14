# Construct the De Bruijn Graph of a Collection of k-mers

"""Given an arbitrary collection of k-mers Patterns (where some k-mers may appear multiple times),
we define CompositionGraph(Patterns) as a graph with |Patterns| isolated edges. 
Every edge is labeled by a k-mer from Patterns, and the starting and ending nodes of an edge are labeled by the prefix and suffix of the k-mer labeling that edge. 
We then define the de Bruijn graph of Patterns, denoted DeBruijn(Patterns), by gluing identically labeled nodes in CompositionGraph(Patterns), which yields the following algorithm."""


import pprint  # to pretty print the output
import pyperclip  # to copy the result to the clipboard


def Prefix(Pattern):
    """Returns the prefix of a k-mer"""
    return Pattern[:-1]


def Suffix(Pattern):
    """Returns the suffix of a k-mer"""
    return Pattern[1:]


def CompositionGraph(Patterns):
    """
    Constructs the CompositionGraph of the collection of k-mers Patterns.
    :param Patterns: A collection of k-mers.
    :return: The composition graph CompositionGraph(Patterns), in the form of a tuple containing (Prefixes, Suffixes).
    """
    # Initialize an empty list to store the edges
    edges = []
    for kmer in Patterns:
        prefix = Prefix(kmer)
        suffix = Suffix(kmer)
        edges.append((prefix, suffix))
    return edges


# Test the CompositionGraph function
listKmer = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
pprint.pp(CompositionGraph(listKmer))


def DeBruijn(Patterns):
    """
    Constructs the de Bruijn graph of a collection of k-mers Patterns.
    :param Patterns: A collection of k-mers.
    :return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
    """
    # Construct the CompositionGraph of Patterns
    edges = CompositionGraph(Patterns)
    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}
    # Iterate over each edge in the CompositionGraph
    for edge in edges:
        # Unpack the edge into the prefix and suffix
        prefix, suffix = edge
        # Check if the prefix is already in the adjacency list
        if prefix in adj_list:
            # Append the suffix to the list of neighbors
            adj_list[prefix].append(suffix)
        else:
            # Initialize a new list with the suffix as the neighbor
            adj_list[prefix] = [suffix]
    # Sort the adjacency list by keys (prefixes) and values (suffixes) in alphabetical order
    sorted_adj_list = {k: sorted(v) for k, v in sorted(adj_list.items())}
    return sorted_adj_list


print("The De Bruijn graph of the given k-mers is:")
pprint.pp(DeBruijn(listKmer))


def adj_list_to_string(overlap_adj_list):
    """Convert the overlap graph to a string representation.

    :param adj_list: The overlap graph in the form of an adjacency list.
    :return: A string representation of the overlap graph.
    """
    return "\n".join(f"{k} -> {', '.join(v)}" for k, v in overlap_adj_list.items())


def read_kmers_from_file(filename):
    """Reads a collection of k-mers from a text file.

    :param filename: The path to the file containing k-mers.
    :return: A list of k-mers.
    """
    with open(filename, "r") as file:
        # remove empty lines and add to list
        kmers = [line.strip() for line in file if line.strip()]

    return kmers


# Example usage
filename = "Devoir/Datasets/05_dataset.txt"  #  file path
kmers = read_kmers_from_file(filename)  # read the k-mers from the file
adj_list = DeBruijn(kmers)  # Construct the overlap graph (adjacency list)
graph_str = adj_list_to_string(adj_list)
# Convert the adjacency list to a string representation

print(graph_str)
pyperclip.copy(graph_str)  # Copy the result to the clipboard
# Check the result on Rosalind : https://rosalind.info/problems/ba3e/
