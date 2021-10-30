farenheit_to_celsius='no'
if farenheit_to_celsius=='yes':
    f=32
    print('The Current Temperature in Flagstaff in degrees Fahrenheit is:')
    print(f)
    c=(f-32)*1.8
    print('The Current Temperature in Flagstff in degrees Celsius is:')
    print(round(c))
else:
    c=100
    print('The Current Temperature in Flagstaff in degrees Celsius is:')
    print(c)
    f=c*1.8+32
    print('The Current Temperature in Flagstaff in degrees Fahrenheit is:')
    print(round(f))
