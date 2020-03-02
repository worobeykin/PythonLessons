#Amount days from birth
from datetime import datetime, timedelta, date


now = datetime.today()

#data = input("Data(yyyy-mm-dd): ")
#data1 = data.split('-')
data1 = ['1998', '06', '13']
birth = datetime(int(data1[0]), int(data1[1]), int(data1[2]))
print(type(birth))
delta = now - birth
print(type(delta))

print(now)
print(delta.days)
print("\n\n")

print(birth.isoweekday())
print(str(int(delta.days)))


count_weekend = 0
all_data = []
for i in range(int(delta.days)+1):
    if birth.isoweekday() == 6 or birth.isoweekday() == 7:
        count_weekend += 1
        
    all_data.append(birth.day)
    birth += timedelta(days=1)
#print(all_data)
print(count_weekend)

















#print("\n\n")
#data2 = datetime.strptime(data, "%Y-%m-%d")

#print(data2)
#delta = now - data2
#print(delta.days)

#Definition weekend amount
