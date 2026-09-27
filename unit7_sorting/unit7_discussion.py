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
    output = lst.copy()

    for i in range(len(output) - 1):
        for j in range(len(output) - i - 1):
            if output[j] > output[j + 1]:
                temp = output[j]
                output[j] = output[j + 1]
                output[j + 1] = temp

    return output


def merge_sort(lst: list) -> list:
    output = lst.copy()

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
    if len(lst) > 1:
        mid = len(lst) // 2
        left_partition = lst[:mid]
        right_partition = lst[mid:]

        merge_sort_recursive(left_partition)
        merge_sort_recursive(right_partition)

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
    left_index = 0
    right_index = 0
    arg_lst_index = 0

    while left_index < len(left_partition) and right_index < len(right_partition):
        if left_partition[left_index] < right_partition[right_index]:
            lst[arg_lst_index] = left_partition[left_index]
            left_index += 1
        else:
            lst[arg_lst_index] = right_partition[right_index]
            right_index += 1
        arg_lst_index += 1

    while left_index < len(left_partition):
        lst[arg_lst_index] = left_partition[left_index]
        left_index += 1
        arg_lst_index += 1

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

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.


    lst = random.sample(range(1, 101), 25)

    merge_sorted_list = merge_sort(lst)
    bubble_sorted_list = bubble_sort(lst)

    print(lst)
    print(merge_sorted_list)
    print(bubble_sorted_list)
    
    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

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




if __name__ == "__main__":
    main()
