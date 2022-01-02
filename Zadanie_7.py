if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

suma = 0
for x in student_marks[query_name]:
    suma = suma + x

srednia = suma / 3
print (f'{srednia:.2f}')



