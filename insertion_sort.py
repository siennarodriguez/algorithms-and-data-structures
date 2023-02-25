
def insertion_sort(nums):
    '''
    A simple comparison based sorting algorithm. It inserts every array
    element into its proper position. In i-th iteration, previous (i-1) elements
    (i.e. subarray Arr[1:(i-1)]) are already sorted. The i-th element (Arr[i]) is
    inserted into its proper place in the previously sorted subarray

    Parameters:
        nums: (int) array of items 
    
    Returns: 
        nums: (int) array of items sorted in acending order
    
    Time complexity:
        Best case: O(N) - sorted array on input and O(1) swaps
        Worst case: O(N^2) - reversely sorted and inner loops makes max comparisons
        Average case: O(N^2) 

    Space complexity: O(1) auxiliary - in-place sort.
    '''
    for i in range(1, len(nums)):
        current = nums[i]

        j = i-1 #previous num
        while j>=0 and current < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current

    return nums

def main():
    nums = [5,2,3,1]
    insertion_sort(nums)
    print(nums)

main()