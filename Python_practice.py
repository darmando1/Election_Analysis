import csv
import os


csvpath = os.path('..','Election_Analysis','election_results.csv')
with open(csvpath) as election_data:
    csvreader = csv.reader(election_data)
    print(next(row(1)))
