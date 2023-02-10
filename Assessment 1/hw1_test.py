"""
Xuqing Wu
CSE 163 AA

below are the test functiuon and main method to test
whether the function results of hw1 are correct
"""
import hw1

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits() -> None:
    """
    Tests the count_divisible_digits method
    """
    # The regular case
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(3, hw1.count_divisible_digits(999, 9))
    assert_equals(0, hw1.count_divisible_digits(-124, 7))

    # Test the m = 0 case
    assert_equals(0, hw1.count_divisible_digits(1, 0))


def test_is_relatively_prime() -> None:
    """
    Tests the is_relatively_prime method
    """
    # The given cases
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    # 2 additional tests
    assert_equals(False, hw1.is_relatively_prime(2, 8))
    assert_equals(False, hw1.is_relatively_prime(3, 9))


def test_travel() -> None:
    """
    Tests the travel method
    """
    # The given cases
    assert_equals((-1, 4), hw1.travel('NW!ewnW', (1, 2)))
    # 2 additional tests
    assert_equals((1, 2), hw1.travel('Nne!', (0, 0)))
    assert_equals((1, 2), hw1.travel('Nnew', (1, 0)))


def test_reformat_date() -> None:
    """
    Tests the reformat_date method
    """
    # The given cases
    assert_equals("31/12/1998",
                  hw1.reformat_date("12/31/1998", "M/D/Y", "D/M/Y"))
    assert_equals("3/1/2", hw1.reformat_date("1/2/3", "M/D/Y", "Y/M/D"))
    assert_equals("4/0", hw1.reformat_date("0/200/4", "Y/D/M", "M/Y"))
    assert_equals('2', hw1.reformat_date("3/2", "M/D", "D"))
    # 2 additional tests
    assert_equals('9/10', hw1.reformat_date("10/9/6", "M/D/Y", "D/M"))
    assert_equals('1/2/3', hw1.reformat_date("1/2/3", "M/D/Y", "M/D/Y"))


def test_longest_word() -> None:
    """
    Tests the longest_word method
    """
    # The given case
    assert_equals('3: Merrily,', hw1.longest_word('/home/song.txt'))
    # 2 additional tests
    assert_equals('4: thought', hw1.longest_word('/home/song2.txt'))
    assert_equals('2: flashback', hw1.longest_word('/home/song3.txt'))


def test_get_average_in_range() -> None:
    """
    Tests the get_average_in_range method
    """
    # regular cases
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0666666, hw1.get_average_in_range([1, 2, 3.2], -1, 10))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 2], 2, 3))
    # test 0 return
    assert_equals(0, hw1.get_average_in_range([1, 2, 3], 90, 200))


def test_mode_digit() -> None:
    """
    Tests the mode_digit method
    """
    # The given case
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    # 2 additional tests
    assert_equals(3, hw1.mode_digit(111222333))
    assert_equals(0, hw1.mode_digit(1000001))


def main():
    test_total()
    # Call your test functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()
