def bubble_sort(list):
    '''
    Repeatedly compares and swaps (if needed) adjacent elements in every pass.
    In i-th pass of Bubble Sort, last (i-1) elements are already sorted and
    the i-th largest element is placed at the i-th last position.

    Parameters:
        nums: (int) array of items 
    
    Returns: 
        nums: (int) array of items sorted in acending order

    Time complexity:
        Best case: O(N) - Sorted array as input and O(1) swaps
        Worst case: O(N^2) - reversely sorted/very few elements
                            are in proper place
        Average case: O(N^2) 

    Space complexity: O(1) auxiliary - a temp var is used in swapping (in-place sort)
    '''
    n = len(list)

    for i in range (n-1):
        for j in range(n-1):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list

def main():
    list = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    bubble_sort(list)
    print(list)

    list = [3, 9, 2, 1]
    bubble_sort(list)
    print(list)

main()