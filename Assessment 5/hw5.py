"""
Xuqing Wu
CSE 163 AA

This file contains the implementations of this homework.
We analyze and plot geospatial data to investigate food
deserts in Washington. “Food deserts” are neighborhoods
where residents do not have nearby access to grocery stores
offering affordable and nutritious food.

The dataset we use is the joint of 2010 US census data with
food access data. A census tract is defined as a food desert if
enough people in the tract do not have nearby access to food
sources.
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def load_in_data(shp_file_name: str, csv_file_name: str) -> gpd.GeoDataFrame:
    '''
    takes in a CSV(food access dataset) and an SHP(census dataset) file
    and merges them to create a GeoDataFrame.
    '''
    census = gpd.read_file(shp_file_name)
    food_access = pd.read_csv(csv_file_name)
    merge = census.merge(food_access, left_on='CTIDFP00',
                         right_on='CensusTract', how='left')
    return merge


def percentage_food_data(state_data: gpd.GeoDataFrame) -> float:
    '''
    Takes the merged data and returns the percentage of census tracts in
    Washington for which we have food access data. The percentage it
    a float between 0 and 100. Result not rounded.
    '''
    return float(state_data['CensusTract'].dropna().size /
                 state_data['CTIDFP00'].size * 100)


def plot_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes the merged data and plots the shapes of all the census tracts
    in Washington in a file map.png.
    '''
    state_data.plot()
    plt.title("Washington State")
    plt.savefig("map.png")


def plot_population_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes the merged data and plots the shapes of all the census tracts in
    Washington in a file population_map.png where each census tract is
    colored according to population.
    '''
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color='#EEEEEE')
    state_data.dropna().plot(column='POP2010', ax=ax, legend=True)
    plt.title('Washington Census Tract Populations')
    plt.savefig('population_map.png')


def plot_population_county_map(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes the merged data and plots the shapes of all the census tracts in
    Washington in a file county_population_map.png where each county is
    colored according to population.
    '''
    county = state_data[['County', 'POP2010', 'geometry']]
    pop = county.dissolve(by='County', aggfunc='sum')
    fig, ax = plt.subplots(1)
    county.plot(ax=ax, color='#EEEEEE')
    pop.dropna().plot(column='POP2010', ax=ax, legend=True)
    plt.title('Washington County Populations')
    plt.savefig('county_population_map.png')


def plot_food_access_by_county(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes the merged data and produces 4 plots on the same figure showing
    information about food access across income level.
    '''
    county = state_data[['County', 'geometry', 'POP2010', 'lapophalf',
                         'lapop10', 'lalowihalf', 'lalowi10']]
    result = county.dropna()
    result = result.dissolve(by='County', aggfunc='sum')
    result['lapophalf_ratio'] = result['lapophalf'] / result['POP2010']
    result['lapop10_ratio'] = result['lapop10'] / result['POP2010']
    result['lalowihalf_ratio'] = result['lalowihalf'] / result['POP2010']
    result['lalowi10_ratio'] = result['lalowi10'] / result['POP2010']
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    county.plot(color='#EEEEEE', ax=ax1)
    result.plot(column='lapophalf_ratio', legend=True, ax=ax1, vmin=0,
                vmax=1)
    ax1.set_title('Low Access: Half')
    county.plot(color='#EEEEEE', ax=ax2)
    result.plot(column='lalowihalf_ratio', legend=True, ax=ax2, vmin=0,
                vmax=1)
    ax2.set_title('Low Access + Low Income: Half')
    county.plot(color='#EEEEEE', ax=ax3)
    result.plot(column='lapop10_ratio', legend=True, ax=ax3, vmin=0,
                vmax=1)
    ax3.set_title('Low Access: 10')
    county.plot(color='#EEEEEE', ax=ax4)
    result.plot(column='lalowi10_ratio', legend=True, ax=ax4, vmin=0,
                vmax=1)
    ax4.set_title('Low Access + Low Income: 10')
    fig.savefig('county_food_access.png')


def plot_low_access_tracts(state_data: gpd.GeoDataFrame) -> None:
    '''
    Takes the merged data and plots all census tracts considered “low
    access” in a file low_access.png.
    '''
    filtered = state_data[['County', 'geometry', 'POP2010',
                           'lapophalf', 'lapop10', 'Urban', 'Rural']]
    urban = filtered['Urban'] == 1.0
    rural = filtered['Rural'] == 1.0
    urban_low = (filtered['lapophalf'] >= 500) |\
        (filtered['lapophalf'] / filtered['POP2010'] >= 0.33)
    rural_low = (filtered['lapop10'] >= 500) |\
        (filtered['lapop10'] / filtered['POP2010'] >= 0.33)
    low = filtered.loc[(urban & urban_low) | (rural & rural_low)]
    fig, ax = plt.subplots(1)
    state_data.plot(color='#EEEEEE', ax=ax)
    filtered.dropna().plot(color='#AAAAAA', ax=ax)
    low.plot(ax=ax)
    plt.title('Low Access Census Tracts')
    fig.savefig('low_access.png')


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
