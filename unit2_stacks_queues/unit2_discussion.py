"""
### Discussion Board reflection

I have had very limited exposure to stack and queues previously, so this assignment
gave me a lot of insight on how to work with these data structures. This week also 
gave me insight into the usefulness of the pre-made classes that come with the 
"standard libraries" of both python and Java; it made me realize that implementing 
the nuts and bolts myself might not yield the results that are as fast or efficient
and what is already made. One of the challenges I ran into when implementing my real 
world example was python's typing. Although the program does work, I wrote the program
the same way I would write a generic class in Java and my IDE kept falsely identifying
errors.

I really liked the way this week's lab incorporated stacks and queues into the same
trouble ticket class. A queue was used to prioritize which trouble ticket should be 
resolved first, enabling whoever submits a ticket first will get helped first. Then 
when the ticket was resolved, it was placed into a stack, which enabled the ability
to call back the last trouble ticket completed, which is a sort-of "undo" function. 
"""

from collections import deque
from datetime import datetime

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

class TodoItem:
    """A todo item class (real world example)
    
    Attributes:
        title: the title of the todo item
        creation_datetime: the date and time the todo item was generated
        completion_datetime: the date and time the todo item was completed
    """
    def __init__(self, title:str):
        """Initializes a todo instance

        After each todo is Initialized, the datetime is saved to creation_datetime.

        Args:
            title: the title of the todo instance
        """
        self._creation_datetime = datetime.now()
        self._title = title
        self._completion_datetime = ""

    def get_creation_datetime(self):
        """Returns the todo's creation datetime
        """
        return self._creation_datetime

    def get_title(self):
        """Returns the todo's title
        """
        return self._title

    def get_completion_datetime(self):
        """Returns the todo's completion datetime
        """
        return self._completion_datetime

    def update_completion_datetime(self):
        """updates the todo's completion date to the current datetime
        """
        self._completion_datetime = datetime.now()
    
    def reset_completion_datetime(self):
        """resets the completion datetime
        """
        self._completion_datetime = ""

class TodoList:
    """A todo list class, contains todo item objects (real world example)

    Attributes:
        task_queue: the todo list's Queue instance, contains non-completed items
        complete_stack: Stack instance, contains completed items
    """
    def __init__(self, *args):
        """Initializes a Todo list

        Args:
            args must be strings separated by commas, each arg will be made into Todo
            items and added to the task queue

        Raises:
            ValueError: if one or more of the args are not strings
        """
        self._task_queue = Queue()
        self._complete_stack = Stack()
        if len(args) > 0:
            for i in args:
                if type(i) is str:
                    self._task_queue.enqueue(TodoItem(i))
                else:
                    raise ValueError("arg must be a string.")

    def get_todo_length(self):
        """Returns the length of task queue
        """
        return len(self._task_queue)
    
    def get_comleted_length(self):
        """Returns the length of the complete task stack
        """
        return len(self._complete_stack)

    def add_todo(self, title:str):
        """Add an item to the todo list

        Args:
            title: the title of the new todo task

        Raises:
            ValueError: if one or more of the args are not strings
        """
        if type(title) is str:
            self._task_queue.enqueue(TodoItem(title))
        else:
            raise ValueError("arg must be a string.")

    def complete_todo(self):
        """Removes a todo, updates completion date, then adds it to completed stack
        
        Returns:
            "todo list is empty": if the todo list is currently empty

            if the task queue is not empty, it will remove the head, add it to the 
            completed stack, then return the todo's title and completion datetime
        """
        if self._task_queue.is_empty():
            return "todo list is empty"
        else:
            todo = self._task_queue.dequeue()
            todo.update_completion_datetime()
            msg = f"{todo.get_title()}, completed on {todo.get_completion_datetime()}"
            self._complete_stack.push(todo)
            return msg

    def peek_todo(self):
        """Returns the title of the next task in the task queue
        """
        if self._task_queue.is_empty():
            return "todo list is empty"
        else:
            return f"Next Task: {self._task_queue.front().get_title()}, Creation Date: {self._task_queue.front().get_creation_datetime()}"

    def undo_completion(self):
        """Undoes the last task completion

        Removes the todo from the completed stack, resets the completion date, then
        puts it in the back of the queue

        Returns:
            bool: False if stack is empty, True otherwise
        """
        if self._complete_stack.is_empty():
            return False
        else:
            todo = self._complete_stack.pop()
            todo.reset_completion_datetime()
            self._task_queue.enqueue(todo)
            return True

    def view_last_completion(self):
        """Returns a string of the last completed task
        """
        return f"Last complete task: {self._complete_stack.peek().get_title()}, Completed on: {self._complete_stack.peek().get_completion_datetime()}"

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

    print("\n=== Real World Examle: Todo List ===")

    todo_list = TodoList("task1", "task2", "task3")

    print(todo_list.peek_todo())

    print(todo_list.complete_todo())

    print(todo_list.view_last_completion())

    todo_list.undo_completion()

    print(todo_list.peek_todo())
if __name__ == "__main__":
    main()
