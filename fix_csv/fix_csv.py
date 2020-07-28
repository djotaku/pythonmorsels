import argparse
import csv

parser = argparse.ArgumentParser(description="Change CSV delimiters")
parser.add_argument('original', help="The original CSV file to convert")
parser.add_argument('destination', help="The destination CSV file, comma delimited")
args = parser.parse_args()

with open(args.original) as csv_file:
    original_input = list(csv.reader(csv_file, delimiter='|'))

with open(args.destination, 'w') as csv_file:
    output_writer = csv.writer(csv_file, delimiter=',')
    output_writer.writerows(original_input)