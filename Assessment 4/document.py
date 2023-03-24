"""
Xuqing Wu
CSE 163 AA

This file represents a single document in the SearchEngine.
"""


from cse163_utils import normalize_token


class Document:
    """
    The class that includs methods to compute term frequency, and
    it is also used to let the SearchEngine class build on.
    """
    def __init__(self, path: str) -> None:
        """
        The initializer that takes a path to a document and
        initializes the document data.
        Assume that the file exists, but that it could be empty.
        """
        self._path: str = path
        self._num_words: int = 0
        # contruct term frequency for each term in the document
        self._freq: dict[str, float] = {}
        content = ''
        with open(path) as f:
            content = f.read()
            word_list = content.split()
            self._num_words = len(word_list)
            for token in word_list:
                token = normalize_token(token)
                if token in self._freq:
                    self._freq[token] += 1
                else:
                    self._freq[token] = 1
        for key in self._freq.keys():
            self._freq[key] = float(self._freq[key] / self._num_words)

    def term_frequency(self, term: str) -> float:
        """
        returns the term frequency of a given term. The function would
        handle the given term, so it does not have to be case sensitive,
        and could contain punctuations. If a term does not appear in a
        given document, it should have a term frequency of 0.
        """
        term = normalize_token(term)
        if term not in self._freq:
            return 0
        else:
            return self._freq[term]

    def get_path(self) -> str:
        """
        returns the path of the file that this document represents
        """
        return self._path

    def get_words(self) -> list[str]:
        """
        returns a list of the unique, normalized words in this document
        """
        return list(self._freq.keys())

    def __str__(self) -> str:
        """
        returns a string representation of this document in the format
        "Document({doc_path}, words: {num_words})" where doc_path is
        the path to the document given in the Document initializer and
        where num_words is the total number of words in the document.
        """
        return f"Document({self._path}, words: {self._num_words})"
