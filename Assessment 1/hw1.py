"""
Xuqing Wu
CSE 163 AA

Below are seven functions that utilize different data structures,
takes in numbers, tuples, strings and/or lists
and return expected values to make the main easier to write,
each should be tested on the hw1_test file.
"""


def total(n: int) -> int | None:
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


# Write your functions here!
def count_divisible_digits(n: int, m: int) -> int:
    """
    Take two integer numbers n and m, m is a single digit and
    non negative. Return the count of the digits of n that are
    divivible by m. If the digit is 0, it is divisible by any m.
    If m is 0, returns 0.
    """
    n = abs(n)
    if m == 0:
        return 0
    else:
        num = 0
        while n // 10 > 0:
            digit = n % 10
            n = n // 10
            if digit == 0:
                num += 1
            elif digit % m == 0:
                num += 1
        if n == 0:
            num += 1
        elif n % m == 0:
            num += 1
        return num


def is_relatively_prime(n: int, m: int) -> bool:
    """
    Takes two integer numbers,
    Returns whether they are relatively prime to each other,
    which means share no common factors besides 1.
    n and m are at least 1.
    """
    for i in range(2, n + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True


def travel(direction: str, location: tuple[int, int]) -> tuple[int, int]:
    """
    Takes a string that represents the aimed direction
    such as 'NW!ewnW', where any characters that are not
    'N', 'E', 'W', or 'S' (ignoring letter-casing) should be ignored.
    The directions string uses 'N' to indicate increasing
    the y-coordinate, 'E' to indicate increasing the
    x-coordinate, 'S' to indicate decreasing the y-coordinate,
    and 'W' to indicate decreasing the x-coordinate.
    Also take a tuple consists of two integers representing the
    current location.
    Returns the final location as a tuple in the form of (x_new, y_new)
    after following the directions starting from the given x, y
    in the tuple.
    """
    direction = direction.lower()
    x_cord_change = 0
    y_cord_change = 0
    for i in range(len(direction)):
        if direction[i] == 'n':
            y_cord_change += 1
        elif direction[i] == 'w':
            x_cord_change -= 1
        elif direction[i] == 'e':
            x_cord_change += 1
        elif direction[i] == 's':
            y_cord_change -= 1
    x = location[0] + x_cord_change
    y = location[1] + y_cord_change
    final_location = (x, y)
    return final_location


def reformat_date(date: str, current: str, target: str) -> str:
    """
    Takes three string representing a date, a current date format,
    and a target date format.
    Returns a new string with the date formatted in the target format.
    A date string will be some non-empty string of numbers
    separated by "/" (e.g, "3/6/1995"). The numbers between the /‘s
    can have any number of digits. There is at least one digit for
    each part of the date provided.
    The current and target formats will be some non-empty sequence
    of the characters 'D', 'M', 'Y' separated by "/".
    """
    dat = date.split('/')
    cur = current.split('/')
    result = {}
    for key in cur:
        for value in dat:
            result[key] = value
            dat.remove(value)
            break
    tar = target.split('/')
    final = ''
    for i in tar:
        if i in result:
            final += result.get(i)
            final += '/'
    final = final[:-1]
    return final


def longest_word(file_name: str) -> str | None:
    """
    Takes a string filename
    returns the longest word in the file with which line it appears on
    If there are ties for the longest word,
    return the one that appears first in the file
    If the file is empty or there are no words in the file,
    return None
    """
    with open(file_name) as f:
        lines = f.readlines()
        word_count = 0
        row = 0
        word_row = 0
        max_word = ''
        if len(lines) == 0:
            return None
        else:
            for line in lines:
                row += 1
                words = line.split()
                for word in words:
                    if len(word) > word_count:
                        word_count = len(word)
                        word_row = row
                        max_word = word
            return str(word_row) + ": " + max_word


def get_average_in_range(nums: list[float], low: float, high: float) -> float:
    """
    takes a list of floats, a float low, and a float high
    returns the average of all values within the list that
    lies in the given range
    from low (inclusive) to high (exclusive).
    If there are no values in the given range, returns 0.
    """
    count = 0
    total = 0.0
    for i in nums:
        if i >= low and i < high:
            total += i
            count += 1
    if count == 0:
        return 0
    else:
        average = float(total / count)
        return average


def mode_digit(n: int) -> int:
    """
    takes an integer number n
    returns the digit that appears most frequently in that number
    given number may be positive or negative, but the most frequent digit
    returned should always be non-negative.
    If there is a tie for the most frequent digit,
    the digit with the greatest value should be returned.
    If the taken integer is 0, return 0.
    """
    n = abs(n)
    counts = {}
    while n > 0:
        digit = n % 10
        n = n // 10
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    max_digit = 0
    max_num = 0
    for i in counts.keys():
        is_num_bigger = counts.get(i) > max_num
        is_digit_bigger = counts.get(i) == max_num and i > max_digit
        if (is_num_bigger or is_digit_bigger):
            max_digit = i
            max_num = counts.get(i)
    return max_digit
