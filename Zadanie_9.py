def count_substring(string, sub_string):
    count = 0
    fin = 0
    pos = 0

    while fin != 1:
        new_pos = string.find(sub_string, pos, len(string))
        if new_pos == -1:
            fin = 1
            return count
        else:
            count += 1
            pos = new_pos + 1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
