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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def make_set(records):
    incoming_set = set()
    outgoing_set = set()
    for record in records:
        incoming_set.add(record[1])
        outgoing_set.add(record[0])
    return outgoing_set, incoming_set

outgoing_calls, incoming_calls = make_set(calls)
outgoing_texts, incoming_texts = make_set(texts)
marketers = list(outgoing_calls - incoming_calls - incoming_texts - outgoing_texts)
marketers.sort()

print("These numbers could be telemarketers: ")
for num in marketers:
    print(num)
