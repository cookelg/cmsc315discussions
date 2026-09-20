"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Behind the scenes, Python dictionaries are implemented using a hash map. 
    # in a map ADT, value are retrieved using a key rather than an index. A hash
    # in introduced as a way to assign keys to a designated index. When adding 
    # a key-value pair to a python dictionary, a hashing function converts the 
    # key to an unsigned integer, which is then used to determine where the data 
    # is placed using modulo arithmetic. In the example below, the keys are the 
    # names of the points of interest, and the values are a list containing x and 
    # y geographic coordinates. 
    points_of_inteterest = {}

    points_of_inteterest["Walmart"] = [36.75894430333459, -76.00926518440248]
    points_of_inteterest["Target"] = [36.755330146119654, -76.01033806800844]
    points_of_inteterest["Walgreens"] = [36.76073013509644, -76.00599288940431]
    points_of_inteterest["AutoZone"] = [36.7526779490791, -76.01138949394227]
    points_of_inteterest["Chipotle"] = [36.75604453205572, -76.00783288478853]

    for key in points_of_inteterest:
        print(f"{key}: {points_of_inteterest[key]}")


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    poi_list = ["Walmart", "Target"]

    # When a lookup is performed, the lookup key is first converted to a hash. 
    # The hash table will then determine the lookup hash's location on the table,
    # and retrieve the key-value pair located at that index (if one exists). The
    # Existing key and the lookup key are compared, if the existing key == the 
    # lookup key, the existing key's value is returned.
    for poi in poi_list:
        print(f"{poi} is located at coordinates {points_of_inteterest[poi]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    T_X_COORD = -1.117
    T_Y_COORD = -3.14

    # Duplicate keys cannot exist in the same map, they can only be updated. In 
    # a Python dictionary, the same syntax is used to both create a key-value pair
    # and update the value for a given key. In this example, the coordinates
    # for each location have a transformation applied. 
    print("\nBefore Coordinate Transformation:")
    for key in points_of_inteterest:
        print(f"{key}: {points_of_inteterest[key]}")

    for key in points_of_inteterest:
        x_coord = points_of_inteterest[key][0]
        y_coord = points_of_inteterest[key][1]

        points_of_inteterest[key][0] = x_coord + T_X_COORD 
        points_of_inteterest[key][1] = y_coord + T_Y_COORD 

    print("\nAfter Coordinate Transformation:")
    for key in points_of_inteterest:
        print(f"{key}: {points_of_inteterest[key]}")
    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    
    # When a key is removed from a map, so too is the value. If a key is removed
    # from a map, its length is decremented by one. 
    print("\nBefore key removal:")
    for key in points_of_inteterest:
        print(f"{key}: {points_of_inteterest[key]}")

    del points_of_inteterest["Walgreens"]

    print("\nAfter key removal:")
    for key in points_of_inteterest:
        print(f"{key}: {points_of_inteterest[key]}")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: In python, if you attempt to retrieve a non-existant key using 
    # the dict[key] syntax, a KeyError exception will occur. The dict.get(key) 
    # method will return None if the key does not exist
    print(f"lookup 'Walgreens' returns {points_of_inteterest.get("Walgreens")}")
    #
    # Edge case 2: deleting a non-existant key from a dictionary will throw a 
    # KeyError exception and nothing should happen to the remainder of the key-value
    # pairs
    try:
        del points_of_inteterest["Walgreens"]
    except KeyError:
        print("Key does not exist...")




if __name__ == "__main__":
    main()
