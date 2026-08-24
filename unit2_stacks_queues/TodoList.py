from unit2_discussion import Stack, Queue
from datetime import datetime

class TodoItem:
    """A todo item class
    
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
    """A todo list class, contains todo item objects

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
    todo_list = TodoList("task1", "task2", "task3")

    print(todo_list.peek_todo())

    print(todo_list.complete_todo())

    print(todo_list.view_last_completion())

    todo_list.undo_completion()

    print(todo_list.peek_todo())



if __name__ == "__main__":
    main()





