"""
Xuqing Wu
CSE 163 AA

This file represents the SearchEngine class as well as a command-line
interface for using the SearchEngine.
"""


import os
import math
from cse163_utils import normalize_token
from document import Document


def get_tfidf(pair: tuple[Document, float]) -> float:
    """
    takes a tuple of the form (document, float) and return the float.
    We will apply the get_tfidf function on each pair and sort on the
    tfidf_list.
    """
    return pair[1]


class SearchEngine:
    """
    The SearchEngine class represents a corpus of Document objects and
    includes methods to compute the tf–idf statistic between each document
    and a given query.

    tf–idf is a text information statistic for determining the relevance
    of a term to each document from a corpus consisting of many documents.
    """
    def __init__(self, directory: str) -> None:
        """
        takes a str path to a directory. Assume the string represents a
        valid directory, and that the directory contains only valid files.
        Process the content of directories to prepare for other methods.
        """
        self._path: str = directory
        self._num_docs: int = 0
        self._inverted_index: dict[str, list[Document]] = dict()
        all_files = os.listdir(directory)
        list_file = list()
        # contruct the inverted_index for the directory
        for files in all_files:
            path = Document(os.path.join(directory, files))
            list_file.append(path)
            for term in path.get_words():
                if term not in self._inverted_index:
                    self._inverted_index[term] = list()
                self._inverted_index[term].append(path)
        self._num_docs = len(list_file)

    def _calculate_idf(self, term: str) -> float:
        """
        takes a str term and returns the inverse document frequency
        of that term. If the term is not in the corpus, return 0.
        Otherwise, if the term is in the corpus, compute the inverse
        document frequency idf.
        idf(term t)=ln(total number of documents in corpus/
        number of documents containing term t)
        """
        if term not in self._inverted_index.keys():
            return 0
        else:
            contain = len(self._inverted_index[term])
            return math.log(float(self._num_docs / contain))

    def __str__(self) -> str:
        """
        returns a string representation of this SearchEngine in
        the format "SearchEngine({path}, size: {num_docs})" where
        path is the path to the directory given in the initializer
        and where num_docs is the total number of unique documents
        in the corpus.
        """
        return f"SearchEngine({self._path}, size: {self._num_docs})"

    def search(self, query: str) -> list[str]:
        """
        takes a str query that contains one or more terms. The search
        method returns a list of document paths sorted in descending
        order by tf–idf statistic. Normalize the terms before processing.
        If there are no matching documents, return an empty list.
        """
        word_query = query.split()
        tfidf_list = []  # list of tuple(Document, float)
        tfidf_dict = {}  # dictionary {Document, float}
        path_list = []
        se = SearchEngine(self._path)
        for word in word_query:
            word = normalize_token(word)
            if word in self._inverted_index:
                # list of docs that contain word
                docs = self._inverted_index[word]
                for doc in docs:
                    # calculate tfidf for each doc
                    idf = se._calculate_idf(word)
                    df = doc.term_frequency(word)
                    tfidf = idf * df
                    if doc in tfidf_dict:
                        tfidf_dict[doc] += tfidf
                    else:
                        tfidf_dict[doc] = tfidf
        for key in tfidf_dict.keys():
            tfidf_list.append((key, tfidf_dict[key]))
        tfidf_list = sorted(tfidf_list,
                            key=get_tfidf, reverse=True)
        for path in tfidf_list:
            path_list.append(path[0].get_path())
        return path_list
