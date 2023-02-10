"""
Xuqing Wu
CSE 163 AA

below are the test functiuon and main method to test
whether the results are correct
"""
import hw0

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the total method
    """
    """
    The regular case
    """
    assert_equals(15, hw0.total(5))
    """
    Seems likely we could mess up 0 or 1
    """
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    # TODO: add your own total test here


def test_funky_sum() -> None:
    """
    Tests the funky_sum method
    """
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(2.2, hw0.funky_sum(1, 3, 0.6))
    assert_equals(3, hw0.funky_sum(1, 3, 1))


def test_swip_swap() -> None:
    """
    Tests the swip_swap method
    """
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    assert_equals('foobra', hw0.swip_swap('foobar', 'r', 'a'))
    assert_equals('boofar', hw0.swip_swap('foobar', 'f', 'b'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
