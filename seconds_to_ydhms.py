s=31719845
print("The following number of seconds:")
print(s)
year=s// (365*24*3600)
s =s % (365*24*3600)
day=s//(24*3600)
s=s %(24*3600)
hour=s//3600
s%=3600
minutes=s//60
s%=60
seconds=s
print('Is equilvalent to:')
print(year)
print('year')
print(day)
print('days')
print(hour)
print('hours')
print(minutes)
print('minutes')
print(seconds)
print('seconds')
