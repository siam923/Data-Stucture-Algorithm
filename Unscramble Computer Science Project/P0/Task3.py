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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A
def phone_call_from_bangalour(records):
    phone_list = []
    for record in records:
        if record[0].startswith('(080)'):
            receiver = record[1]
            if receiver.startswith('(0'):
                area_code = receiver.split(')')[0][1:]
                if area_code not in phone_list:
                    phone_list.append(area_code)
            elif receiver.startswith('7') or receiver.startswith('8') or receiver.startswith('9'):
                prefix = receiver[0:4]
                if prefix not in phone_list:
                    phone_list.append(prefix)
            elif receiver.startswith('140'):
                if '140' not in phone_list:
                    phone_list.append('140')
    return phone_list


code_list = phone_call_from_bangalour(calls)
code_list.sort()

print("The numbers called by people in Bangalore have codes:")
for code in code_list:
    print(code)


## Part B
def get_percentage(records):
    count = 0
    fixed_line_count = 0
    for record in records:
        # Check if th number is fixed_line
        if record[0].startswith('(080)'):
            fixed_line_count += 1
        # Count for Bangalore -> Bangalore
        if record[0].startswith('(080)') and record[1].startswith('(080)'):
            count += 1
    return 100 * count/fixed_line_count

print("{:.2f} percent of calls from ".format(get_percentage(calls)) +
        "fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
