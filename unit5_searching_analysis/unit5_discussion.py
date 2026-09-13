"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import random
import time
import csv


def linear_search(lst, target) -> int:
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # in a linear search, every value in the list is checked against the target 
    # until a match is found. The worst case is that the value does not exist, 
    # meaning the function checks every index. Therefore, this function has a 
    # time complexity of O(N)
    for i, value in enumerate(lst):
        if target == value:
            return i
    return -1


def binary_search(lst, target) -> int:
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # I chose to use recurstion to implement the Binary Search. This was done using 
    # a helper function.
    return binary_search_recursive(lst, 0, len(lst) - 1, target)


def binary_search_recursive(lst: list, low: int, high: int, target: int) -> int:
    # base case: if low is greater then high, the target is not in list
    if low > high:
        return -1
    # during each recursion, a new mid value is calculated. This will be the index
    # that is compared against the target.
    mid = int((low + high) / 2)
    # If the value at index mix is greater than the target, mid -1 is passed as 
    # the new high index in the next recursion, thereby only passing half of the 
    # list. 
    if lst[mid] > target:
        return binary_search_recursive(lst, low, mid - 1, target)
    # If the value at the mid index is less than the target, mid + 1 is passed as 
    # the new low index in the next recursion, again only passing half of the list.
    elif lst[mid] < target:
        return binary_search_recursive(lst, mid + 1, high, target)
    # if all the above tests return false, then the only other case is that the
    # value at index mid equals the target, and that index is returned.
    else:
        return mid


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # the small dataset is a sorted list of 25 random integers ranging from 1-100.
    lst = sorted(random.sample(range(1, 101), 25))
    print(lst)

    # the starting time is recorded
    start_time = time.perf_counter()

    # Linear Search is about as efficient as Binary Search with small datasets
    # because the number of checks is only slightly more than a Binary Search.
    print(f"7 found at index {linear_search(lst, 7)}")

    # the end time is captured after the process is run
    end_time = time.perf_counter()
    # the total time is calculated by subtracting start time - end time. The
    # output is in seconds
    total_time_sec = end_time - start_time
    #converting seconds to milliseconds
    total_time_milli = total_time_sec * 1000

    print(f"Linear search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Linear time elapsed: {total_time_sec:.6f} seconds")
    start_time = time.perf_counter()
    print(f"7 found at index {binary_search(lst, 7)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000

    # There is no noticeable time difference between linear and binary search
    print(f"Binary search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Binary search time elapsed: {total_time_sec:.6f} seconds")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    start_time = time.perf_counter()
    # the large dataset is a sorted list of 10,000,000 integers ranging in value
    # between 1-30,000,000.
    lst = sorted(random.sample(range(1, 30000001), 10000000))
    end_time = time.perf_counter()

    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    # first time measurement is the total elapsed time taken to sort the large 
    # dataset.
    print("Time elapsed to generate and sort a list of 10,000,000 integers:")
    print(f"-- {total_time_milli:.6f} milliseconds")
    print(f"-- {total_time_sec:.6f} seconds\n")

    # Capture the start time for the linear search
    start_time = time.perf_counter()
    print(f"9,986,500 found at index {linear_search(lst, 9986500)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000

    # Searching for a large value guaruntees that a linear search will take longer
    # to parse. In the case of a large dataset, a linear search takes noticably 
    # longer.
    print(f"Linear search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Linear time elapsed: {total_time_sec:.6f} seconds")

    # Capture the start time for the binary search
    start_time = time.perf_counter()

    # Even for larger values, a binary search takes significantly less time than 
    # linear search. 
    print(f"9,986,500 found at index {binary_search(lst, 9986500)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    print(f"Binary search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Binary search time elapsed: {total_time_sec:.6f} seconds")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    
    # Edge case: search for a string rather than an integer.
    # This edge case also serves as a real-life use case. AI was used to generate 
    # a sorted CSV file with 200 unique emails stored in emails.csv

    email_list = []
    # open emails.csv and create a csv.DictReader object. Then, iterate through 
    # the 'email' column and append the strings to a list.
    with open('emails.csv', mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            email_list.append(row['email'])
    
    start_time = time.perf_counter()

    # This string is an email that is located near the end of the csv file.
    new_email = "z0shzbuk3@protonmail.com"

    # binary_search is called, and the index of the email is stored in a variable
    email_index = binary_search(email_list, new_email)

    # if the email exists, a print statement gives the index of that email
    if email_index > -1:
        print(f"{new_email} located at index {email_index}")
    # if the email does not exits, a message indecates that the email is available
    else:
        print(f"{new_email} is available for use!")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    print(f"Binary search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Binary search time elapsed: {total_time_sec:.6f} seconds")

    start_time = time.perf_counter()

    # an email that is not in the list is passed to binary_search
    new_email = "lawrence@gmail.com"
    email_index = binary_search(email_list, new_email)
    if email_index > -1:
        print(f"{new_email} located at index {email_index}")
    else:
        print(f"{new_email} is available for use!")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    print(f"Binary search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Binary search time elapsed: {total_time_sec:.6f} seconds")





if __name__ == "__main__":
    main()
