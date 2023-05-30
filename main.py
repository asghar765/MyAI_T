# main.py

from table_printer import print_table
from search_engines import search_github, search_huggingface, search_twitter, search_google

def search_and_print(query):
    # Search on GitHub
    github_results = search_github(query)

    # Search on Hugging Face
    huggingface_results = search_huggingface(query)

    # Search on Twitter
    twitter_results = search_twitter(query)

    # Search on Google
    google_results = search_google(query)

    # Combine the results
    all_results = github_results + huggingface_results + twitter_results + google_results

    # Print the table
    print_table(all_results)

if __name__ == "__main__":
    query = input("Enter your search query: ")
    search_and_print(query)
