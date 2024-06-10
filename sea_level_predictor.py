import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    data = data.drop(columns=['NOAA Adjusted Sea Level'])
    print(data.head())
    print(data.dtypes)
    print(data.shape)

    # Create scatter plot
    year = data['Year']
    sea_level = data['CSIRO Adjusted Sea Level']
    plt.scatter(year, sea_level)


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()