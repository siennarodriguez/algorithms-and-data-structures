def selection_sort(list):
    '''
    Selects the i-th smallest element and places at i-th position. 
    This algorithm divides the array into 2 parts: sorted (left) and
    unsorted (right) subarray. It selects the smallest element from the
    unsorted subarray and places in the first position of that subarray
    (ascending order). It repeatedly selects the next smallest element

    Parameters:
        nums: (int) array of items 
    
    Returns: 
        nums: (int) array of items sorted in acending order

    Time complexity:
        Best case: O(N^2) and O(1) swaps
        Worst case: O(N^2) - reversely sorted and inner loops makes max comparisons
        Average case: O(N^2) 

    Space complexity: O(1) auxiliary - in-place sort.
    '''
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