# Place code below to do the analysis part of the assignment.
import csv
dic ={}
with open('/Users/brandongao/hw2/data/clean_data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader, None)

    for row in reader:
        year = int(row[0])
        anomaly = float(row[1])
        decade = (year // 10) * 10
        if decade in dic:
            dic[decade]['total'] += anomaly
            dic[decade]['count'] += 1
        else:
            dic[decade] = {'total': anomaly, 'count': 1}


for decade, data in sorted(dic.items()):
    average_anomaly = data['total'] / data['count']
    print(f"From Decade {decade} to {decade+9}: Average Temperature Anomaly = {average_anomaly:.2f}°F")