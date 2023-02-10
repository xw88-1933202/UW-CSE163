"""
Xuqing Wu
CSE 163 AA

Below are six functions that don't use pandas,
(using Python built-in data structures plus Python math functions)
takes in a list of dictionaries about features of Pokemons
and return some summarized characteristics,
each should be tested on the hw2_test file.
Assume the data is never empty and that there’s no missing data.
"""
from cse163_utils import Pokemon


def species_count(data: list[Pokemon]) -> int:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    returns the number of unique pokemon species in the dataset
    """
    unique_pokemon = set()
    for pokemon in data:
        unique_pokemon.add(pokemon['name'])
    return len(unique_pokemon)


def max_level(data: list[Pokemon]) -> tuple[str, int]:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    returns a 2-element tuple of the (name, level) of the pokemon
    with the highest level in the dataset
    If there is more than one pokemon with the highest level,
    return the pokemon that appears first in the file
    """
    current_level = 0
    current_name = ''
    for pokemon in data:
        if pokemon['level'] > current_level:
            current_level = pokemon['level']
            current_name = pokemon['name']
    return (current_name, current_level)


def filter_range(data: list[Pokemon],
                 lower: int, upper: int) -> list[str]:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    and two integers: a lower bound (inclusive) and upper
    bound (exclusive). Returns a list of the names of pokemon
    whose level fall within the bounds in the same order that
    they appear in the dataset
    """
    filtered = []
    for pokemon in data:
        if pokemon['level'] >= lower and pokemon['level'] < upper:
            filtered.append(pokemon['name'])
    return filtered


def mean_attack_for_type(data: list[Pokemon],
                         pok_type: str) -> float | None:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    and a str representing the pokemon type
    returns the average atk for all the pokemon in the dataset
    with the given type
    If there are no pokemon of the given type, return None
    """
    sum_tot = 0
    count = 0
    for pokemon in data:
        if pokemon['type'] == pok_type:
            sum_tot += pokemon['atk']
            count += 1
    if count == 0:
        return None
    return float(sum_tot / count)


def count_types(data: list[Pokemon]) -> dict[str, int]:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    returns a dictionary representing
    for each pokemon type the number of pokemon of that type.
    The order of the keys in the returned dictionary does not matter.
    """
    result = dict()
    for pokemon in data:
        spec_type = pokemon['type']
        if spec_type in result:
            result[spec_type] += 1
        else:
            result[spec_type] = 1
    return result


def mean_attack_per_type(data: list[Pokemon]) -> dict[str, float]:
    """
    takes a parsed pokemon dataset(a list of dictionaries)
    returns a dictionary representing for each pokemon type
    the average atk of pokemon of that type.
    The order of the keys in the returned dictionary does not matter.
    """
    sum_tot = {}
    count = {}
    for i in range(len(data)):
        types = data[i]['type']
        atk = data[i]['atk']
        if types not in sum_tot:
            sum_tot[types] = 0
            count[types] = 0
        sum_tot[types] += atk
        count[types] += 1
    average = {types: sum_tot[types] / count[types]
               for types in sum_tot.keys()}
    return average
