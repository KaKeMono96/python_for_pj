a = 100
b = 112
c = 101
d = 119
e = 103

if (a > b) and (a > c) and (a > d) and (a > e):
    largestNumber = a
elif (b > a) and (b > c) and (b > d) and (b > e):
    largestNumber = b
elif (c > a) and (c > b) and (c > d) and (c > e):
    largestNumber = c
elif (d > a) and (d > b) and (d > c) and (d > e):
    largestNumber = d
else:
    largestNumber = e
print("LargestNumber is", largestNumber)
