"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_numbers_count(records, phone_no):
    for record in records:
        if record[0] not in phone_no:
            phone_no.append(record[0])
        if record[1] not in phone_no:
            phone_no.append(record[1])

phone_no = []
unique_numbers_count(texts, phone_no)
unique_numbers_count(calls, phone_no)

numbers_count = len(phone_no)
print("There are {} different telephone numbers in the records.".format(numbers_count))
