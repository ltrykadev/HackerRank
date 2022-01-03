def mutate_string(string, position, character):
    l = list(string)            # konwersja na liste
    l[position] = character     # dodanie znaku
    string = ''.join(l)         # konwersja na lancuch
    return string               # zwrocenie zmodyfikowane lancuha

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

