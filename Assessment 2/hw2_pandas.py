"""
Xuqing Wu
CSE 163 AA

Below are six functions that use pandas, and
do not use any loops or list/dictionary comprehensions.
takes in a Pandas DataFrame
and return some summarized characteristics,
each should be tested on the hw2_test file.
Assume the data is never empty and that there’s no missing data.
"""


import pandas as pd


def species_count(df: pd.DataFrame) -> int:
    """
    takes a Pandas DataFrame
    returns the number of unique pokemon species in the dataset
    """
    filtered = df['name'].unique()
    return len(filtered)


def max_level(df: pd.DataFrame) -> tuple[str, int]:
    """
    takes a Pandas DataFrame
    returns a 2-element tuple of the (name, level) of the pokemon
    with the highest level in the dataset
    If there is more than one pokemon with the highest level,
    return the pokemon that appears first in the file
    """
    index = df['level'].idxmax()
    row = df.loc[index]
    return (row['name'], row['level'])


def filter_range(df: pd.DataFrame,
                 lower: int, upper: int) -> list[str]:
    """
    takes a Pandas DataFrame and two integers:
    a lower bound (inclusive) and upper bound (exclusive)
    returns a list of the names of pokemon whose level fall within
    the bounds in the same order that they appear in the dataset
    """
    level_high = df['level'] >= lower
    level_low = df['level'] < upper
    filtered = df[level_high & level_low]
    return filtered['name'].tolist()


def mean_attack_for_type(df: pd.DataFrame,
                         pok_type: str) -> float | None:
    """
    takes a Pandas DataFrame dataset and a string
    representing the pokemon type
    returns the average atk for all the pokemon in the dataset
    with the given type
    If there are no pokemon of the given type, return None
    """
    is_type = df[df['type'] == pok_type]
    atk_mean = is_type['atk'].mean()
    if len(is_type) == 0:
        return None
    return atk_mean


def count_types(df: pd.DataFrame) -> dict[str, int]:
    """
    takes a Pandas DataFrame
    returns a dictionary representing
    for each pokemon type the number of pokemon of that type.
    The order of the keys in the returned dictionary does not matter.
    """
    type_count = df.groupby('type')['type'].count()
    return dict(type_count)


def mean_attack_per_type(df: pd.DataFrame) -> dict[str, float]:
    """
    takes a Pandas DataFrame
    returns a dictionary representing for each pokemon type
    the average atk of pokemon of that type.
    The order of the keys in the returned dictionary does not matter.
    """
    atk_mean = df.groupby('type')['atk'].mean()
    return atk_mean.to_dict()
