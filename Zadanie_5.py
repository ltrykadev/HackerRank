n = int(input())

lista = []
lista = list(map(int, input().strip().split()))[:n]

lista = sorted(set(lista), reverse=True)
print(lista[1])