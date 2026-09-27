"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""
import random
import time


def bubble_sort(lst: list) -> list:
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # a copy of the input list is created to preserve the origianl list
    output = lst.copy()

    # A bubble sort works by iterating through the entire list and swapping values.
    # The bubble sort will not proceed to the next iteration until it locates the 
    # smallest value in the given segment of the list. Once the smallest value is 
    # found, it is swapped to the starting index. Each index of each for loop 
    # evaluates each index of the list, therefore is has a time complexity of 
    # O(N^2)
    for i in range(len(output) - 1):
        for j in range(len(output) - i - 1):
            if output[j] > output[j + 1]:
                temp = output[j]
                output[j] = output[j + 1]
                output[j + 1] = temp

    return output


def merge_sort(lst: list) -> list:
    # the input list is copied to preserve the original list
    output = lst.copy()

    # the copied list is passed to the recursive merge sort function
    merge_sort_recursive(output)

    return output

def merge_sort_recursive(lst: list):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # The base case for the recursive function is if the list length is equal to 1.
    # Once the base case is reached, the current recursion call is terminated and 
    # the previous recursion call continues with the right_partition. Once the base
    # case for the right_partition is reached, both partitions for the current 
    # recursive call are passed to the merge function with the copied list. 
    if len(lst) > 1:
        # Calculate the middle index
        mid = len(lst) // 2
        # Create the left partition by copying from index 0 to mid (inclusive)
        left_partition = lst[:mid]
        # Create the right_partition by copying from the middle index (non-inclusive)
        # to the end of the list.
        right_partition = lst[mid:]

        # call the next recursion for the left_partition
        merge_sort_recursive(left_partition)
        # call the next recursion for the right_partition
        merge_sort_recursive(right_partition)

        # pass both partitions to the merge function
        merge(lst, left_partition, right_partition)



def merge(lst: list, left_partition: list, right_partition: list):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # left_index is the iterator used only for the left_partition
    left_index = 0
    # right_index is the iterator used only for the right_partition
    right_index = 0
    # arg_lst_index is the iterator used only for the list from the previous
    # recursion call
    arg_lst_index = 0

    # iterate each partition and compare the two values from each list. The while 
    # loop will terminate when either list's index reaches the end of its partinion.
    # The lowest of the two compared values will be passed to the argument list.
    while left_index < len(left_partition) and right_index < len(right_partition):
        if left_partition[left_index] < right_partition[right_index]:
            lst[arg_lst_index] = left_partition[left_index]
            left_index += 1
        else:
            lst[arg_lst_index] = right_partition[right_index]
            right_index += 1
        arg_lst_index += 1

    # If the right partition reaches the end of its list caused the previous while 
    # loop to break, all remaining values from the left_partition are added to the 
    # previous recursion call's array. 
    while left_index < len(left_partition):
        lst[arg_lst_index] = left_partition[left_index]
        left_index += 1
        arg_lst_index += 1

    # If the left partition reaches the end of its list caused the first while 
    # loop to break, all remaining values from the right_partition are added to the 
    # previous recursion call's array. 
    while right_index < len(right_partition):
        lst[arg_lst_index] = right_partition[right_index]
        right_index += 1
        arg_lst_index += 1


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    lst = random.sample(range(1, 101), 25)
    print(lst)

    print("\nBubble Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    bubble_sorted_list = bubble_sort(lst)


    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(bubble_sorted_list)
    print(f"Bubble sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Bubble sort time elapsed: {total_time_sec:.6f} seconds\n")

    print("\nMerge Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    merge_sorted_list = merge_sort(lst)

    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(merge_sorted_list)
    print(f"Bubble sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Bubble sort time elapsed: {total_time_sec:.6f} seconds\n")



    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.
    
    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    lst2 = random.sample(range(1, 30001), 10000)
    mid = len(lst2) // 2

    print(f"list 2 length: {len(lst2)}")
    print(f"First 10 values: {lst2[:10]}")
    print(f"Middle 10 values: {lst2[mid:mid + 10]}")
    print(f"Last 10 values: {lst2[len(lst2) - 11:]}")
    print("\nBubble Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    bubble_sorted_list = bubble_sort(lst2)


    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(f"First 10 values: {bubble_sorted_list[:10]}")
    print(f"Middle 10 values: {bubble_sorted_list[mid:mid + 10]}")
    print(f"Last 10 values: {bubble_sorted_list[len(lst2) - 11:]}")
    print(f"Bubble sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Bubble sort time elapsed: {total_time_sec:.6f} seconds\n")

    print("\nMerge Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    merge_sorted_list = merge_sort(lst2)

    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(f"First 10 values: {merge_sorted_list[:10]}")
    print(f"Middle 10 values: {merge_sorted_list[mid:mid + 10]}")
    print(f"Last 10 values: {merge_sorted_list[len(lst2) - 11:]}")
    print(f"Merge sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Merge sort time elapsed: {total_time_sec:.6f} seconds\n")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    
    # Edge case: sorting a list that contains all duplicate values.
    
    lst3 = [0] * 1000
    mid = len(lst3) // 2

    print(f"list 2 length: {len(lst3)}")
    print(f"First 10 values: {lst3[:10]}")
    print(f"Middle 10 values: {lst3[mid:mid + 10]}")
    print(f"Last 10 values: {lst3[len(lst3) - 11:]}")
    print("\nBubble Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    bubble_sorted_list = bubble_sort(lst3)


    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(f"First 10 values: {bubble_sorted_list[:10]}")
    print(f"Middle 10 values: {bubble_sorted_list[mid:mid + 10]}")
    print(f"Last 10 values: {bubble_sorted_list[len(lst3) - 11:]}")
    print(f"Bubble sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Bubble sort time elapsed: {total_time_sec:.6f} seconds\n")

    print("\nMerge Sort start")
    # the starting time is recorded
    start_time = time.perf_counter()

    merge_sorted_list = merge_sort(lst3)

    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(f"First 10 values: {merge_sorted_list[:10]}")
    print(f"Middle 10 values: {merge_sorted_list[mid:mid + 10]}")
    print(f"Last 10 values: {merge_sorted_list[len(lst3) - 11:]}")
    print(f"Merge sort time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Merge sort time elapsed: {total_time_sec:.6f} seconds\n")




if __name__ == "__main__":
    main()
