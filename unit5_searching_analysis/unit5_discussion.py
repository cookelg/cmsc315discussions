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
    return binary_search_recursive(lst, 0, len(lst) - 1, target)


def binary_search_recursive(lst: list, low: int, high: int, target) -> int:
    if low > high:
        return -1
    mid = int((low + high) / 2)
    if lst[mid] > target:
        return binary_search_recursive(lst, low, mid - 1, target)
    elif lst[mid] < target:
        return binary_search_recursive(lst, mid + 1, high, target)
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

    lst = sorted(random.sample(range(1, 101), 25))
    print(lst)
    start_time = time.perf_counter()
    print(f"7 found at index {linear_search(lst, 7)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    print(f"Linear search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Linear time elapsed: {total_time_sec:.6f} seconds")
    start_time = time.perf_counter()
    print(f"7 found at index {binary_search(lst, 7)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
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

    lst = sorted(random.sample(range(1, 30001), 10000))

    start_time = time.perf_counter()
    print(f"9876 found at index {linear_search(lst, 9876)}")
    end_time = time.perf_counter()
    total_time_sec = end_time - start_time
    total_time_milli = total_time_sec * 1000
    print(f"Linear search time elapsed: {total_time_milli:.6f} milliseconds")
    print(f"Linear time elapsed: {total_time_sec:.6f} seconds")
    start_time = time.perf_counter()
    print(f"9876 found at index {binary_search(lst, 9876)}")
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


if __name__ == "__main__":
    main()
