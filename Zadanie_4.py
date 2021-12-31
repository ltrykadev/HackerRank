import re

if __name__ == '__main__':
    count = int(input())
    number = input()

if len(number) == 10:
    print("YES")
else:
    print("No")

match = re.search(r'^[789]', number)
if match:
    print("match!")
else:
    print("no match!")