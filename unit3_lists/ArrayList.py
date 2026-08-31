"""
### Discussion Board reflection
1. What concepts or skills did you lear while completing this assignment?
This assignment forced me to really focus on what is happening with memory when 
a list ADT is at work. It helped me step out of my comfort zone and really see what
goes on under the hood for seemingly simple data storing tasks.

2. What challenges did you encounter, and how did you overcome them?
The biggest challenge I ran into with this discussion was attempting to implement a 
linked list class. I spun my wheel for a few hours trying to get it to work in Python,
but I couldn't figure out how to get Python to allocate a linked list instance 
with pointers to null nodes for the head and tail. It seems like when python refers
to something as None, it doesn't see it as a placeholder in memory like in Java. I 
couldn't figure out how to get this right, so I just moved on to implementing an 
ArrayList class. You can review my source code for the linked list class and let 
me know what I did wrong.

3. Linked lists and array list ADT's can affect real-world applications in different
ways depending on their use case. For example, a linked list will be able to populate
new data a lot more efficiently because adding a new data item to an existing list 
only requires two pointers to be updated. On the other hand, an array list ADT might 
have to iterate through and shift a large number of existing items to make room. The
array list makes up for this by allowing for efficient sorting algorithms that a 
linked list cannot support.

"""
class ArrayList:
    """An Array list class

    Attributes:
        alloc_size (int): the total number of allocations for the list
        length (int): the total number of items in the list
        _arr (list): the Python list that contains the items
    """
    def __init__(self, start_size:int) -> None:
        """Initializes an ArrayList instance

        The ArrayList is initialized with a length of zero, and the number of
        allocated spaces is given as an argument

        Attributes:
            start_size (int): the starting number of allocations in the list
        """
        self.alloc_size: int = start_size
        self.length:int = 0
        self._arr = []

    def __str__(self) -> str:
        return f"{self._arr.__str__()}\n allocation size: {self.alloc_size}, length: {self.length}\n"

    def __len__(self):
        return len(self._arr)

    def append(self, data):
        """Appends data to the end of the list

        If the length of the list is as long as alloc_size, the allocation is
        doubled
        
        Attributes:
            data: the item to be added to the list
        """
        if self.length == self.alloc_size:
            self.resize(self.length * 2)
        self._arr.append(data)
        self.length += 1

    def prepend(self, data):
        """Prepends data to the beginning of the list

        If the length of the list is as long as alloc_size, the allocation is
        doubled
        
        Attributes:
            data: the item to be added to the list
        """
        if self.length == self.alloc_size:
            self.resize(self.length * 2)
        self._arr.insert(0, data)
        self.length += 1

    def resize(self, new_alloc_size: int):
        """Adds additional allocations to the ArrayList

        Attributes:
            new_alloc_size (int): the new allocation size of the ArrayList
        """
        self.alloc_size = new_alloc_size

    def insert_at(self, index:int, data):
        """Inserts data to a specified index

        If the length of the list is as long as alloc_size, the allocation is
        doubled

        Attributes:
            index (int): the index at which the data will be added
            data: the data to be added to the ArrayList
        """
        if index > self.length:
            raise ValueError("The index is out of range")
        if self.length == self.alloc_size:
            self.resize(self.length * 2)
        self._arr.insert(index, data)
        self.length += 1

    def remove_at(self, index:int):
        """Removes data from a specified index

        Attributes:
            index (int): the index from which data will be removed
        Returns:
            returns the item removed from the ArrayList
        Raises:
            ValueError: if the index argument is beyond the range of the ArrayList
        """
        if index + 1 > self.length:
            raise ValueError("The index is out of range")
        item = self._arr[index]
        del self._arr[index]
        self.length -= 1
        return item

    def search(self, item):
        """Searches the ArrayList for the provided argument
        Attributes:
            item: the data to be searched for
        Returns:
            If the item exists, returns the index of the item
            If the item does not exist, returns -1
        Raises:
            ValueError: if the index argmument is beyond the range of the ArrayList
        """
        for i in range(0, self.length):
            if self._arr[i] == item:
                return i
        return -1

