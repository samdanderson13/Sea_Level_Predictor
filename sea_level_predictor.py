import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    data = data.drop(columns=['NOAA Adjusted Sea Level'])

    # Create scatter plot
    year = data['Year']
    sea_level = data['CSIRO Adjusted Sea Level']
    plt.scatter(year, sea_level)

    # Create first line of best fit
    line_one = linregress(year, sea_level)
    slope = line_one.slope
    intercept = line_one.intercept

    left_x = data['Year'][0]
    left_y = slope * left_x + intercept

    right_x = 2050
    right_y = slope * right_x + intercept

    x = [left_x,right_x]
    y = [left_y,right_y]

    plt.plot(x, y)

    # Create second line of best fit
    trunc_data = data[data['Year'] >= 2000]
    trunc_year = trunc_data['Year']
    trunc_sea_level = trunc_data['CSIRO Adjusted Sea Level']
    
    line_two = linregress(trunc_year, trunc_sea_level)
    slope = line_two.slope
    intercept = line_two.intercept

    left_x = 2000
    left_y = slope * left_x + intercept

    right_x = 2050
    right_y = slope * right_x + intercept

    x = [left_x,right_x]
    y = [left_y,right_y]

    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()