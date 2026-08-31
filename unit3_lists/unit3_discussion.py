"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
from ArrayList import ArrayList

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===\n")
    # instantiate a new ArrayLIst object
    test_list1 = ArrayList(4)
    # prints the __str__() information for the ArraList object, list is empty
    print(test_list1) 
    # appends the number 15, list is empty, therefore its stored at index 0
    test_list1.append(15)
    print(test_list1)
    # appends "item1" to the ArrayList, stored at index 1
    test_list1.append("item1")
    print(test_list1)
    # appends 1.11 to the ArrayList, stored at index 2
    test_list1.append(1.11)
    print(test_list1)
    # inserts "item2" to the ArrayList at index 2, stored at index 2. Max length reached
    test_list1.insert_at(2, "item2")
    print(test_list1)
    # re-allocated 2x more space in the ArrayList, adds "item3" to index 0
    test_list1.prepend("item3")
    print(test_list1)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    print(test_list1)
    print(f"{test_list1.remove_at(0)} was deleted from the beginning")
    print(test_list1)
    print(f"{test_list1.remove_at(int(len(test_list1) / 2))} was deleted from the middle")
    print(test_list1)
    print(f"{test_list1.remove_at(len(test_list1) - 1)} was deleted from the end")
    print(test_list1)
    

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # searches for item1 in the list, the search should be successful
    print("Search for item1 was",
          f"{f"Successful, index {test_list1.search("item1")}" if test_list1.search("item1") >= 0 
          else "unsuccessful, the item is not in the list" }")
    # searches for item2 in the list, the search should be unsuccessful
    print("Search for item2 was",
          f"{f"Successful, index {test_list1.search("item2")}" if test_list1.search("item2") >= 0 
          else "unsuccessful, the item is not in the list" }")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # when prompted to insert an item at an index that is out of range, the method 
    # should throw an exception
    try:
        test_list1.insert_at(3, "item3")
        print(test_list1)
    except ValueError as error:
        print(error)

    # when prompted to remove an item at an index that is out of range, the method 
    # should throw an exception
    try:
        test_list1.remove_at(3)
        print(test_list1)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
