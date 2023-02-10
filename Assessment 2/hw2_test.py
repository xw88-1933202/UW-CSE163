"""
Xuqing Wu
CSE 163 AA

below are the test functiuons and main method to test
whether the function results of hw2_manual and
hw2_pandas are correct, with respect to 2 csv test files,
one is given and one is created by myself.
"""
import pandas as pd

from cse163_utils import assert_equals, parse, Pokemon

import hw2_manual
import hw2_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"      # import files
SELF_TEST_FILE = "/home/test_2.csv"


# Your tests here!
def test_species_count(spec_test_df: pd.DataFrame,
                       spec_test_data: list[Pokemon],
                       my_test_df: pd.DataFrame,
                       my_test_data: list[Pokemon]) -> None:
    '''
    test the species_count method
    '''
    assert_equals(3, hw2_pandas.species_count(spec_test_df))
    assert_equals(3, hw2_manual.species_count(spec_test_data))
    assert_equals(5, hw2_pandas.species_count(my_test_df))
    assert_equals(5, hw2_manual.species_count(my_test_data))


def test_max_level(spec_test_df: pd.DataFrame,
                   spec_test_data: list[Pokemon],
                   my_test_df: pd.DataFrame,
                   my_test_data: list[Pokemon]) -> None:
    '''
    test the max_level method
    '''
    assert_equals(('Lapras', 72), hw2_pandas.max_level(spec_test_df))
    assert_equals(('Lapras', 72), hw2_manual.max_level(spec_test_data))
    assert_equals(('Magmar', 96), hw2_pandas.max_level(my_test_df))
    assert_equals(('Magmar', 96), hw2_manual.max_level(my_test_data))


def test_filter_range(spec_test_df: pd.DataFrame,
                      spec_test_data: list[Pokemon],
                      my_test_df: pd.DataFrame,
                      my_test_data: list[Pokemon]) -> None:
    '''
    test the filter_range method
    '''
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(spec_test_df, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(spec_test_data, 35, 72))
    assert_equals(['Magmar', 'Porygon'],
                  hw2_pandas.filter_range(my_test_df, 90, 100))
    assert_equals(['Magmar', 'Porygon'],
                  hw2_manual.filter_range(my_test_data, 90, 100))


def test_mean_attack_for_type(spec_test_df: pd.DataFrame,
                              spec_test_data: list[Pokemon],
                              my_test_df: pd.DataFrame,
                              my_test_data: list[Pokemon]) -> None:
    '''
    test the mean_attack_per_type method
    '''
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(spec_test_df, 'fire'))
    assert_equals(47.5,
                  hw2_manual.mean_attack_for_type(spec_test_data, 'fire'))
    assert_equals(62,
                  hw2_pandas.mean_attack_for_type(my_test_df, 'fire'))
    assert_equals(62,
                  hw2_manual.mean_attack_for_type(my_test_data, 'fire'))


def test_count_types(spec_test_df: pd.DataFrame,
                     spec_test_data: list[Pokemon],
                     my_test_df: pd.DataFrame,
                     my_test_data: list[Pokemon]) -> None:
    '''
    test the count_types method
    '''
    assert_equals({'fire': 2, 'water': 2},
                  hw2_pandas.count_types(spec_test_df))
    assert_equals({'fire': 2, 'water': 2},
                  hw2_manual.count_types(spec_test_data))
    assert_equals({'fire': 1, 'normal': 1, 'grass': 1, 'bug': 2},
                  hw2_pandas.count_types(my_test_df))
    assert_equals({'fire': 1, 'normal': 1, 'grass': 1, 'bug': 2},
                  hw2_manual.count_types(my_test_data))


def test_mean_attack_per_type(spec_test_df: pd.DataFrame,
                              spec_test_data: list[Pokemon],
                              my_test_df: pd.DataFrame,
                              my_test_data: list[Pokemon]) -> None:
    '''
    test the mean_attack_per_type method
    '''
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_pandas.mean_attack_per_type(spec_test_df))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  hw2_manual.mean_attack_per_type(spec_test_data))
    assert_equals({'fire': 62, 'normal': 68,
                   'grass': 149, 'bug': 13.5},
                  hw2_pandas.mean_attack_per_type(my_test_df))
    assert_equals({'fire': 62, 'normal': 68,
                   'grass': 149, 'bug': 13.5},
                  hw2_manual.mean_attack_per_type(my_test_data))


def main():
    '''
    Loads in the dataframe and list. Calls all the
    functions above to complete tests.
    '''
    spec_test_df = pd.read_csv(SPEC_TEST_FILE)
    spec_test_data = parse(SPEC_TEST_FILE)
    my_test_df = pd.read_csv(SELF_TEST_FILE)
    my_test_data = parse(SELF_TEST_FILE)
    test_species_count(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_max_level(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_filter_range(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_mean_attack_for_type(spec_test_df, spec_test_data, my_test_df,
                              my_test_data)
    test_count_types(spec_test_df, spec_test_data, my_test_df, my_test_data)
    test_mean_attack_per_type(spec_test_df, spec_test_data, my_test_df,
                              my_test_data)


if __name__ == '__main__':
    main()
