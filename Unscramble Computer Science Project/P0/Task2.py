"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

call_time = {}

for record in calls:
    if record[0] in call_time:
        call_time[record[0]] += int(record[3])
    else:
        call_time[record[0]] = int(record[3])
    if record[1] in call_time:
        call_time[record[1]] += int(record[3])
    else:
        call_time[record[1]] = int(record[3])


phone_num = max(call_time, key=call_time.get)
time_spent = call_time[phone_num]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            phone_num, time_spent))
