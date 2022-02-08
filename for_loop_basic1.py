
1
for x in range(0,151):
    print(x)

2
for x in range(5,1001):
    if x % 5 == 0:
        print(x)

3
for x in range(1,101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

4
oddtotal = 0
for x in range(0,500001):
    if x % 2 == 1:
        oddtotal = oddtotal + x
print(oddtotal)

5
for x in range(2018, 0, -4):
    print(x)

6
lowNum = 10
highNum = 100
mult = 4

for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)