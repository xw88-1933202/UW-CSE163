"""
Xuqing Wu
CSE 163 AA

below are the 6 functions and the main method. Each
function takes in a dataframe and either return a
new dataframe or plot graphs with repect to requirements.
"""
import pandas as pd
import seaborn as sns

# Your imports here
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

sns.set()


# Define your functions here
def compare_bachelors_1980(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Takes the data and computes the percentages of men and women
    who achieved a minimum degree of a Bachelor’s degree in 1980.
    Return a 2-by-2 DataFrame with rows corresponding to men and
    women and columns corresponding to Sex and Total. The order
    of the rows doesn’t matter.
    '''
    is_1980 = df['Year'] == 1980
    male_and_female = df['Sex'] != 'A'
    is_bachelor = df['Min degree'] == "bachelor's"
    filtered = df[is_1980 & male_and_female & is_bachelor]
    return filtered[['Sex', 'Total']]


def top_2_2000s(df: pd.DataFrame, sex: str = 'A') -> pd.Series:
    '''
    Takes two arguments, the data and a sex parameter, and
    computes the two most commonly earned degrees for that
    given sex between the years 2000 and 2010 (inclusive).
    sex should have a default value of 'A' if it is not specified.
    Return a 2-element Series. Compare educational attainment
    levels by using the mean. The index of the returned Series
    should be the Min degree and the values should be its mean.
    '''
    after_2000 = df['Year'] >= 2000
    before_2010 = df['Year'] <= 2010
    is_sex = df['Sex'] == sex
    filtered = df[after_2000 & before_2010 & is_sex]
    all_val = filtered.groupby('Min degree')['Total'].mean()
    return all_val.nlargest(2)


def line_plot_bachelors(df: pd.DataFrame) -> None:
    '''
    takes the data and plots a line chart of the total
    percentages of all people Sex A with bachelor's Min
    degree over time. Label the x-axis Year, the y-axis
    Percentage, and title the plot Percentage Earning
    Bachelor’s over Time. Save the plot as line_plot_bachelors.png.
    '''
    is_student = df['Sex'] == 'A'
    min_bachelor = df['Min degree'] == "bachelor's"
    filtered = df[is_student & min_bachelor]
    sns.relplot(x='Year', y='Total', data=filtered, kind="line")
    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df: pd.DataFrame) -> None:
    '''
    takes the data and plots a bar chart comparing
    the total percentages of Sex F, M, and A with high
    school Min degree in the Year 2009. Label the x-axis
    Sex, the y-axis Percentage, and title the plot Percentage
    Completed High School by Sex. Save the plot as
    bar_chart_high_school.png
    '''
    is_2009 = df['Year'] == 2009
    is_high_school = df['Min degree'] == 'high school'
    filtered = df[is_2009 & is_high_school]
    sns.catplot(x='Sex', y='Total', data=filtered, kind="bar")
    plt.title('Percentage Completed High School by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df: pd.DataFrame) -> None:
    '''
    takes the data and plots how the percentage of all Hispanic
    students with degrees have changed between 1990–2010 (inclusive)
    for high school and bachelor's Min degree. Label the axes and
    title the plot appropriately. Save the plot as
    plot_hispanic_min_degree.png
    '''
    after_1990 = df['Year'] >= 1990
    before_2010 = df['Year'] <= 2010
    is_high = df['Min degree'] == 'high school'
    is_ba = df['Min degree'] == "bachelor's"
    filtered = df[after_1990 & before_2010 & (is_high | is_ba)]
    is_hispanic = filtered[filtered['Hispanic'].notnull()]
    sns.relplot(data=is_hispanic, x="Year", y="Hispanic", hue="Min degree",
                kind="line", ci=None)
    plt.title("Percentage of Hispanics with high school"
              " and bachelor's as min degree over time")
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(df: pd.DataFrame) -> float:
    '''
    The aim is to Train a DecisionTreeRegressor to predict
    the percentage of degrees attained for a given Sex, Min
    degree, and Year. Takes the data and returns the test mean
    squared error as a float.
    '''
    df = df[['Year', 'Min degree', 'Sex', 'Total']]
    df = df.dropna()
    features = df.loc[:, df.columns != 'Total']
    labels = df['Total']
    features = pd.get_dummies(features)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2, random_state=2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)
    return mean_squared_error(labels_test, predictions)


def main():
    '''
    Loads in the dataset provided and calls all the 6
    functions above. For all of the method calls, rely on
    any default parameters we specified.
    '''
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    # Call your functions here
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
