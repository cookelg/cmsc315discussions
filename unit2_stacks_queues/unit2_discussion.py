"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    """Stack Class

    A generic stack class that demonstrates last in, first out behavior.

    Attributes:
        Stack.instance_count (int): The number of instantiated stack objects
        _stack_deque (collections.deque): The Stack uses an instance of the Deque class
        _stack_id (int): The Stack's unique identifier
    """
    instance_count = 0

    def __init__(self, *args):
        """Initializes a Stack instance

        After each stack initialization, Stack.instance_count is incremented by 1
        and the new value is assigned to self._stack_id. Any number of arguments can 
        be passed into the constructor separated by commas, each argument will be 
        added to the Stack in order. 

        Args:
            args*: arguments must be separated by commas,
        """
        Stack.instance_count += 1
        self._stack_deque = deque(args)
        self._stack_id = Stack.instance_count


    def get_stack_id(self):
        """Returns the Stack instance ID
        """
        return self._stack_id

    def __len__(self):
        """Overloaded length operator, Returns the length of the stack instance
        """
        return len(self._stack_deque)

    def push(self, value):
        """Pushes data onto the stack instance

        the data will be placed on the top of the stack and will be the first to be
        removed/returned from pop()

        Args:
            value: data to be pushed onto the stack, can be of any type.
        
        Raises:
            ValueError: if value is null or contains an empty string.

        """
        if value is None: 
            raise ValueError("Input cannot be empty")
        elif type(value) is str and len(value.strip()) == 0:
            raise ValueError("Input cannot be an empty string")
        else:
            self._stack_deque.append(value)

    def pop(self):
        """Removes and reurns the item at the top of the Stack

        the last item that was added to the Stack will be removed and returned.

        Returns:
            "Pop failed, the stack is empty": if the stack instance in empty

            if the stack in not empty, the last item added to the stack will be
            returned.

        """
        if self.is_empty():
            return "Pop failed, the stack is empty."
        else:
            return self._stack_deque.pop()

    def peek(self):
        """Return the item at the top of the Stack.

        The last item that was added to the Stack will be returned, and not removed.

        Returns:
            "Peek failed, the stack is empty.": if the stack is instance is empty.

            if the stack is not empty, the last item added to the stack will be
            returned

        """
        if self.is_empty():
            return "Peek failed, the stack is empty."
        else:
            return self._stack_deque[len(self._stack_deque) - 1]

    def is_empty(self):
        """Determines if the Stack is empty

        Returns:
            bool: True is the Stack is empty, False otherwise
        """
        return len(self._stack_deque) == 0


class Queue:
    """Queue Class

    A generic queue class that demonstrates first in, first out behavior.

    Attributes:
        Queue.instance_count (int): The number of instantiated queue objects
        _queue_deque (collections.deque): The queue uses an instance of the Deque class
        _queue_id (int): The Queue's unique identifier
    """
    instance_count = 0

    def __init__(self, *args):
        """Initializes a Queue instance

        After each queue initialization, Queue.instance_count is incremented by 1
        and the new value is assigned to self._queue_id. Any number of arguments can 
        be passed into the constructor separated by commas, each argument will be 
        added to the Stack in order. 

        Args:
            args*: arguments must be separated by commas,
        """
        Queue.instance_count += 1
        self._queue_deque = deque(args)
        self._queue_id = Queue.instance_count

    def __len__(self):
        """Overloaded length operator, Returns the length of the Stack instance
        """
        return len(self._queue_deque)

    def get_queue_id(self):
        """Returns the Queue's instance ID
        """
        return self._queue_id

    def enqueue(self, value):
        """Appends data onto the back of the Queue instance

        the data will be placed in the back of the queue and will be the last to be
        removed/returned from dequeue()

        Args:
            value: data to be pushed onto the queue, can be of any type.
        
        Raises:
            ValueError: if value is null or contains an empty string.

        """
        if value is None: 
            raise ValueError("Input cannot be empty")
        elif type(value) is str and len(value.strip()) == 0:
            raise ValueError("Input cannot be an empty string")
        else:
            self._queue_deque.append(value)

    def dequeue(self):
        """Removes and returns the item at the front of the Queue

        the first item that was added to the queue will be removed and returned.

        Returns:
            "the queue is empty": if the queue instance in empty

            if the queue in not empty, the item at the front of the queue will be
            returned.

        """
        if self.is_empty():
            return "the queue is empty."
        else:
            return self._queue_deque.popleft()

    def front(self):
        """Return the item at the front of the Queue.

        The first item that was added to the Queue will be returned, and not removed.

        Returns:
            "The queue is empty.": if the queue instance is empty.

            if the queue is not empty, the first item added to the queue will be
            returned

        """
        if self.is_empty():
            return "the queue is empty."
        else:
            return self._queue_deque[0]

    def is_empty(self):
        """Determines if the Queue is empty

        Returns:
            bool: True is the Queue is empty, False otherwise
        """
        return len(self._queue_deque) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TEST1: Create a Stack object, demonstrate LIFO behavior,\n")

stack1 = Stack()

print(f"Stack{stack1.get_stack_id()} Pushing item {len(stack1) + 1}")
stack1.push("item one")
print(f"Stack{stack1.get_stack_id()} Pushing item {len(stack1) + 1}")
stack1.push("item two")
print(f"Stack{stack1.get_stack_id()} Pushing item {len(stack1) + 1}")
stack1.push("item three")
print(f"Stack{stack1.get_stack_id()} Pushing item {len(stack1) + 1}")
stack1.push("item four")

print(f"Stack{stack1.get_stack_id()} peeked item {{ {stack1.peek()} }},",
      f"length of stack after peek: {len(stack1)}")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length of stack after peek: {len(stack1)}")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length of stack after peek: {len(stack1)}")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length of stack after peek: {len(stack1)}")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length of stack after peek: {len(stack1)}")

print("\nTEST2: test popping from an empty stack,")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length: {len(stack1)}")

print("\nTEST3: test peeking at an empty stack,")
print(f"Stack{stack1.get_stack_id()} peeked item {{ {stack1.peek()} }},",
      f"length: {len(stack1)}")

print("\nTEST4: verify a single-item stack becomes empty after removal.")
print(f"Stack{stack1.get_stack_id()} Pushing item {len(stack1) + 1}")
stack1.push("item one")
print(f"Stack{stack1.get_stack_id()} popped item {{ {stack1.pop()} }},",
      f"length: {len(stack1)}")


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TEST1: Create a Queue object, demonstrate FIFO behavior,")

queue1 = Queue()

print(f"Queue{queue1.get_queue_id()}: Queueing item {len(queue1) + 1}")
queue1.enqueue("item 1")
print(f"Queue{queue1.get_queue_id()}: Queueing item {len(queue1) + 1}")
queue1.enqueue("item 2")
print(f"Queue{queue1.get_queue_id()}: Queueing item {len(queue1) + 1}")
queue1.enqueue("item 3")
print(f"Queue{queue1.get_queue_id()}: Queueing item {len(queue1) + 1}")
queue1.enqueue("item 4")

print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")
print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")
print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")
print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")
print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")
print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")
print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")
print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")

print("\nTEST2: test dequeuing from an empty queue,")

print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")

print("\nTEST3: test viewing the front of an empty queue,")

print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")

print("\nTEST4: verify a single-item queue becomes empty after removal.")

print(f"Queue{queue1.get_queue_id()}: Queueing item {len(queue1) + 1}")
queue1.enqueue("item 1")
print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")
print(f"Dequeued {{ {queue1.dequeue()} }}, from Queue{queue1.get_queue_id()}")
print(f"Front of Queue{queue1.get_queue_id()}: {{ {queue1.front()} }}, ",
    f"Length of Queue: {len(queue1)}")

if __name__ == "__main__":
    main()
