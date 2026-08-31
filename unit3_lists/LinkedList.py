from typing import Optional

class LinkedListNode:

    next: LinkedListNode | None
    previous: LinkedListNode | None
    def __init__(self, data: Optional[int]) -> None:
        self.data = data
        self.next: LinkedListNode | None = None
        self.previous: LinkedListNode | None = None

class LinkedList:

    # _head: LinkedListNode
    # _tail: LinkedListNode

    def __init__(self) -> None:
        self._head = LinkedListNode(None)
        self._tail = LinkedListNode(None)
        pass

    def __len__(self) -> int:
        count = 0
        node = self._head
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self) -> str:
        if self._head.next.data == None:
            return "empty list"
        else:
            return self.to_str_recurse(self._head.next)

    def to_str_recurse(self, node:LinkedListNode):
        return f"{node.data}, {self.to_str_recurse(node.next)}"

    def append(self, data:int) -> None:
        self.appendNode(LinkedListNode(data))
    
    def appendNode(self, newNode:LinkedListNode) -> None: 
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            newNode.previous = self._tail
            self._tail = newNode

    def prepend(self, data:int):
        self.prependNode(LinkedListNode(data))

    def prependNode(self, newNode:LinkedListNode) -> None:
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        else:
            self._head.previous = newNode
            newNode.next = self._head
            self._head = newNode

    def ll_search(self, data_value:int) -> LinkedListNode:
        return self._recursive_search(self._head, data_value) 

    def _recursive_search(self, node:LinkedListNode, data_value:int) -> LinkedListNode:
        if node != None:
            if node.data == data_value:
                return node
            return self._recursive_search(node.next, data_value)
        return None

    def insert_after(self, existing_item:int, new_item:int) -> bool:
        existing_node = self.ll_search(existing_item)
        if existing_node != None:
            new_node = LinkedListNode(new_item)
            self._insert_node_after(existing_node, new_node)
            return True
        return False

    def _insert_node_after(self, current_node:LinkedListNode, 
                          new_node:LinkedListNode) -> None:
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        elif current_node == self._tail:
            self._tail.next = new_node
            new_node.previous = self._tail
            self._tail = new_node
        else:
            successsor = current_node.next
            new_node.next = successsor
            new_node.previous = current_node
            current_node.next = new_node
            successsor.previous = new_node

    def remove(self, item_to_remove:int) -> bool:
        removal_node = self.ll_search(item_to_remove)
        if removal_node != None:
            self._remove_node(removal_node)
            return True
        return False

    def _remove_node(self, current_node:LinkedListNode) -> None:
        successor = current_node.next
        predecessor = current_node.previous
        if successor != None:
            successor.previous = predecessor
        if predecessor != None:
            predecessor.next = successor
        if current_node == self._head:
            self._head = successor
        if current_node == self._tail:
            self._tail = predecessor

if __name__ == "__main__":
    int_linkedList = LinkedList()

    int_linkedList.append(5)
    int_linkedList.append(6)
    int_linkedList.append(7)

    print(int_linkedList)
    print(f"5 was removed: {int_linkedList.remove(5)}")
    print(int_linkedList)
    print(f"9 was removed: {int_linkedList.remove(9)}")
    print(int_linkedList)







    



