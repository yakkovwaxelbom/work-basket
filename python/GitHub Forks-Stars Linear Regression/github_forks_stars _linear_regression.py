import itertools
import requests
from tqdm import tqdm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# API URL for GitHub repositories search
API_URL = "https://api.github.com/search/repositories?" + \
          "q=language:{}&sort=stars&per_page=100&page={}"


# Function to get GitHub data (forks and stars) for a specific programming language
def get_github_data(language: str, page):
    """
    Fetch GitHub repositories data for the specified programming language and pages.

    Args:
    language (str): The programming language to filter repositories by.
    page (int): The number of pages to fetch (each page contains 100 repositories).

    Returns:
    tuple: Two lists, one containing forks (x) and the other containing stars (y).
    """
    x = []  # List for forks
    y = []  # List for stars
    for i in tqdm(range(1, page + 1)):  # Fetch data from multiple pages
        response = requests.get(API_URL.format(language, i))  # API call
        if response.status_code == 200:
            data = response.json()  # Get JSON data
            items = data['items']  # Get the list of repositories
            # Extract forks and stars from each repository
            forks = [[item['forks_count']] for item in items]
            stars = [item['stargazers_count'] for item in items]
            x.extend(forks)  # Add forks data to x
            y.extend(stars)  # Add stars data to y
    return x, y


# Function to calculate linear regression using forks as x and stars as y
def calc_liner_regression(x, y):
    """
    Perform linear regression on the given data (forks and stars).

    Args:
    x (list): List of fork counts (independent variable).
    y (list): List of star counts (dependent variable).

    Returns:
    tuple: Coefficient (a), intercept (b), and R² score of the linear regression model.
    """
    reg = LinearRegression().fit(x, y)  # Perform linear regression
    score = reg.score(x, y)  # Calculate R² score
    a = reg.coef_[0]  # Slope (coefficient)
    b = reg.intercept_  # Intercept
    return a, b, score


# Function to display the results of linear regression
def dis_play(x, y, a, b, score):
    """
    Visualize the linear regression results.

    Args:
    x (list): Fork counts.
    y (list): Star counts.
    a (float): Slope of the regression line.
    b (float): Intercept of the regression line.
    score (float): R² score of the regression model.
    """
    # Convert list of lists (forks) to a flat list
    for_find_max = list(itertools.chain(*x))
    ref_line_x = [0, max(for_find_max)]  # X-axis reference points for regression line
    ref_line_y = [b, max(for_find_max) * a + b]  # Y-axis reference points for regression line
    plt.title(f'Error range is {score:.4f}')  # Set plot title with R² score
    plt.plot(ref_line_x, ref_line_y, label='line regression')  # Plot regression line
    plt.scatter(x, y, label='forks and stars')  # Scatter plot of forks and stars
    plt.xlabel("forks")  # X-axis label
    plt.ylabel('stars')  # Y-axis label
    plt.show()  # Show plot


# Main function to fetch data, compute linear regression, and visualize results
def main(language, page):
    """
    Main function to execute the GitHub data retrieval and linear regression analysis.

    Args:
    language (str): The programming language to search repositories for.
    page (int): The number of GitHub API pages to fetch (100 repositories per page).
    """
    x, y = get_github_data(language, page)  # Fetch forks and stars data
    a, b, score = calc_liner_regression(x, y)  # Perform linear regression
    dis_play(x, y, a, b, score)  # Display the regression results


# Entry point of the script
if __name__ == '__main__':
    main('python', 1)  # Fetch data for Python repositories and analyze
