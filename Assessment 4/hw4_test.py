"""
Xuqing Wu
CSE 163 AA

This is the file to test whether the document and
search engine classes work. I create my own txt file
"document_test" to check the results for every method
in document class, and created my own folder "search_
engine_test to check the results for every method in
search_engine class.
"""
import math
from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


# Define your test functions here!
def test_document() -> None:
    """
    Tests the methods in Document file
    """
    doc = Document("/home/document_test.txt")
    # test the term_frequency method
    assert_equals(0.6, doc.term_frequency("row"))
    # test the get_path method
    assert_equals("/home/document_test.txt", doc.get_path())
    # test the get_words method
    assert_equals(['row', 'your', 'boat'], doc.get_words())
    # test the __str__ method
    assert_equals("Document(/home/document_test.txt, words: 5)", str(doc))


def test_search_engine() -> None:
    """
    Tests the methods in search_engine file
    """
    engine = SearchEngine("/home/search_engine_test")
    # test the _calculate_idf method
    assert_equals(math.log(3), engine._calculate_idf("dogs"))
    # test the __str__ method
    assert_equals("SearchEngine(/home/search_engine_test, size: 3)",
                  str(engine))
    # test the search method
    assert_equals(["/home/search_engine_test/doc3.txt",
                   "/home/search_engine_test/doc2.txt",],
                  engine.search("love dogs"))


def main():
    # Call your test functions here!
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
