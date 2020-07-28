import argparse
import csv

parser = argparse.ArgumentParser(description="Change CSV delimiters")
parser.add_argument('original', help="The original CSV file to convert")
parser.add_argument('destination', help="The destination CSV file, comma delimited")
parser.add_argument('--in-delimiter', help="The character for the delimiter in your input file")
parser.add_argument('--in-quote', help="The quote character in the in-file")
args = parser.parse_args()

infile_delimiter = "|"
infile_quote = '\"'

if args.in_delimiter:
    infile_delimiter = args.in_delimiter

if args.in_quote:
    infile_quote = args.in_quote

with open(args.original) as csv_file:
    original_input = list(csv.reader(csv_file, delimiter=infile_delimiter, quotechar=infile_quote))

with open(args.destination, 'w') as csv_file:
    output_writer = csv.writer(csv_file, delimiter=',')
    output_writer.writerows(original_input)