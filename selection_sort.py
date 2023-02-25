def selection_sort(list):
    n = len(list)

    for i in range(n-1):
        min = i

        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        if min != 1:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

    return list

def main():
    list = [3, 9, 2, 1]
    selection_sort(list)
    print(list)

main()