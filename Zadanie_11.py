if __name__ == '__main__':
    s = input()

isalnum = 0
isalpha = 0
isdigit = 0
islower = 0
isupper = 0

list = list(s)

for x in range(len(list)):
    if list[x].isalnum() == True:
        isalnum = 1
    if list[x].isalpha() == True:
        isalpha = 1
    if list[x].isdigit() == True:
        isdigit = 1
    if list[x].islower() == True:
        islower = 1
    if list[x].isupper() == True:
        isupper = 1

if isalnum == 1:
    print('True')
else:
    print('False')

if isalpha == 1:
    print('True')
else:
    print('False')

if isdigit == 1:
    print('True')
else:
    print('False')

if islower == 1:
    print('True')
else:
    print('False')

if isupper == 1:
    print('True')
else:
    print('False')