"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""
import random


class Node:
    def __init__(self, value: int):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value: int = value
        self.left: Node = None
        self.right: Node = None
        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root: Node = None

    def insert(self, value) -> bool:
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The value is first checked if the BST has a root, if false a Node is
        # instantiated with the argument and made into the root. The BST is
        # then checked if the value already exists in the BST, if true then
        # the value is not added and False is returned. If the value does not
        # exist in the BST, then a Node is instatiated with the value and
        # passed into the recursive method. Starting from the root, if the
        # value is greater than that node's value, the new node is passed along
        # to node.right; it is passed to node.left if the new nodes value is
        # less than. This process continues until a null node.left or
        # node.right is found, after which the new node is added.
        if self.root is None:
            self.root = Node(value)
            return True
        elif self.search(value):
            return False
        else:
            self._insert_recursive(self.root, Node(value))
            return True

    def _insert_recursive(self, node: Node, new_node: Node):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if new_node.value < node.value:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_recursive(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_recursive(node.right, new_node)

    def search(self, value: int) -> bool:
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is more efficient than linear search because in the worst
        # case scenario for a linear search, all instances are checked making
        # it O(N) efficiency. BST search on the other hand will only ever need
        # to check one instance per level, making it O(log_{2}N) efficiency.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Node, value: int) -> bool:
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # base case of the recursion is when a leaf is reached, indicating
        # that no matches have been found, returning False.
        if node is None:
            return False
        # Once the value is found, True is returned and the recursion ends
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self) -> list:
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        lst = []
        return self._inorder_recursive(self.root, lst)

    def _inorder_recursive(self, node, values) -> list:
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # the recursion base case is when the leaf is reached, and the method
        # is called on a null Node.
        if node is not None:
            # once the left-most node is reached, this indicates the lowest
            # value for the subtree and the recursive method will append that
            # node to the list.
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            # after the value is appended, the right branch of the subtree is
            # recursed. if there are no left branches, the value will be
            # appended.
            self._inorder_recursive(node.right, values)
            return values


def display_tree(node, level=0, prefix="Root:  "):
    """Recursively displays the tree structure rotated 90 degrees.

    NOTE: this implementation came from a Google Gemini search."""
    if node is not None:
        # Print the right subtree first (so it appears on top when looking
        # sideways)
        display_tree(node.right, level + 1, " /R---")

        # Print the current node with level indentation
        print("|       " * level + prefix + str(node.value))

        # Print the left subtree
        display_tree(node.left, level + 1, " \\L___")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search
    #    space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    bst1 = BST()

    values = random.sample(range(1, 101), 10)

    for i in values:
        # The BST is able to quickly find where to insert each value because it
        # only needs to visit one node per level
        print(f"inserting {i}, {bst1.insert(i)}")

    display_tree(bst1.root)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # The traversal works be recursively finding the left-most node for each
    # sub-tree
    ordered_bst = bst1.inorder()

    print("BST 1 listed in order:")
    print(ordered_bst)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    bst2 = BST()

    values = [50, 49, 51, 17, 11, 89, 1, 44]
    for i in values:
        bst2.insert(i)
        print(f"Adding {i} to BST 2")
    print("BST 2 tree:")
    display_tree(bst2.root)

    # 17 is in the BST, this should return true
    print(f"Value 17 in BST?: {bst2.search(17)}")
    # 25 is not in the BST, this should return false
    print(f"Value 25 in BST?: {bst2.search(25)}")
    # 11 is in the BST, this should return true
    print(f"Value 11 in BST?: {bst2.search(11)}")
    # 99 is not in the BST, this should return false
    print(f"Value 99 in BST?: {bst2.search(99)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    bst3 = BST()

    bst3.insert(50)
    print("\nAdded 50 to BST 3")
    print("BST 3 tree:")
    display_tree(bst3.root)

    # Adding duplicate values to the BST will not work because the insert
    # method checks if the value exists and will not run if true
    print("Attempting to add 50 again to BST 3")
    print(f"bst3.insert(50) returned {bst3.insert(50)}\n")

    # the BST should appear the same as before
    print("BST 3 tree after insert attempt:")
    display_tree(bst3.root)

    # Adding 51 after 50 will result in 51 being added to the right branch
    print("Attempting to add 51 to BST 3")
    print(f"bst3.insert(51) returned {bst3.insert(51)}\n")
    # Adding 49 after 50 will result in 49 being added to the left branch
    print("Attempting to add 49 to BST 3")
    print(f"bst3.insert(49) returned {bst3.insert(49)}\n")
    print("BST 3 tree after insert attempt:")
    display_tree(bst3.root)


if __name__ == "__main__":
    main()
