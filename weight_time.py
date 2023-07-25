import csv
from datetime import date, datetime, time

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Random\weight_time2.csv") as new_csv:
    csv_obj = csv.DictReader(new_csv)
    line_count = 0
    csv_dict = {}
    for row in csv_obj:
        csv_dict[line_count] = row
        line_count += 1

#print(new_dict[0].values())
#set1 = list(csv_dict[0].values())
#print(set1)

#format data so time is time, date is date, weight is int
def clean_data(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        for k, x in value.items():
            value[k] = 0
            if k == "weight":
                value[k] = int(x)
            elif k == "time":
                newval = datetime.strptime(x, "%H:%M:%S").time()
                value[k] = newval
            elif k == "date":
                newval = datetime.strptime(x, "%d/%m/%Y").date()
                value[k] = newval
            else:
                value[k] = x
        new_dict[key] = value
    return new_dict
clean_dict = clean_data(csv_dict)

#prints out all the times, dates, weights - depending on input
def print_data(dictionary, string):
    for key, value in dictionary.items():
        running_time = dictionary[key]
        for key, value in running_time.items():
            if key == string:
                print(value,",",type(value))

#calculate time per weight
#   BUT should really output the full dictionary with the mins per kg added, rather than a new mini dictionary
#   this will allow the other details to be used in the print_results function further down
def calculate_time_per_weight(dictionary):
    tpw_dict = {}
    for key, value in dictionary.items():
        running_time = dictionary[key]
        new_key = running_time["date"]
        time_obj = running_time["time"]
        minutes = time_obj.minute + (time_obj.second / 60)
        tpw = minutes / running_time["weight"]
        tpw_dict[new_key] = tpw
    return tpw_dict
mins_per_kg = calculate_time_per_weight(clean_dict)
print(mins_per_kg)

#do some kind of print as part of a sentence "At DATE, your time was X per kg"
def print_results(dictionary):
    for key, value in dictionary.items():
        date = key.strftime("%d/%m/%Y")
        print("On "+str(date)+", you ran at "+str(value)+" mins per kg.")
print_results(mins_per_kg)       

#write the sentences to a txt file and export it?

#write the time per weight as a new column inside the original CSV?

#How to use date functions - syntax
#x = date(2020, 5, 8)
#y = x.replace(year=2009, day=9)
#z = x.month
#print(z)
#print(type(y))