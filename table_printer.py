# table_printer.py

def print_table(results):
    # Import the necessary libraries
    from tabulate import tabulate

    # Create a table from the results
    table = []
    for result in results:
        table.append([result['source'], result['title'], result['link']])

    # Print the table
    print(tabulate(table, headers=['Source', 'Title', 'Link'], tablefmt='fancy_grid'))
