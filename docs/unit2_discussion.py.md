<!-- markdownlint-disable -->

<a href="../unit2_stacks_queues/unit2_discussion.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `unit2_discussion.py`
### Discussion Board reflection 

I have had very limited exposure to stack and queues previously, so this assignment gave me a lot of insight on how to work with these data structures. This week also  gave me insight into the usefulness of the pre-made classes that come with the  "standard libraries" of both python and Java; it made me realize that implementing  the nuts and bolts myself might not yield the results that are as fast or efficient and what is already made. One of the challenges I ran into when implementing my real  world example was python's typing. Although the program does work, I wrote the program the same way I would write a generic class in Java and my IDE kept falsely identifying errors. 

I really liked the way this week's lab incorporated stacks and queues into the same trouble ticket class. A queue was used to prioritize which trouble ticket should be  resolved first, enabling whoever submits a ticket first will get helped first. Then  when the ticket was resolved, it was placed into a stack, which enabled the ability to call back the last trouble ticket completed, which is a sort-of "undo" function.  


---

<a href="../unit2_stacks_queues/unit2_discussion.py#L367"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

## <kbd>class</kbd> `Queue`
Queue Class 

A generic queue class that demonstrates first in, first out behavior. 



**Attributes:**
 
 - <b>`Queue.instance_count (int)`</b>:  The number of instantiated queue objects 
 - <b>`_queue_deque`</b> (collections.deque):  The queue uses an instance of the Deque class 
 - <b>`_queue_id`</b> (int):  The Queue's unique identifier 

<a href="../unit2_stacks_queues/unit2_discussion.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(*args)
```

Initializes a Queue instance 

After each queue initialization, Queue.instance_count is incremented by 1 and the new value is assigned to self._queue_id. Any number of arguments can  be passed into the constructor separated by commas, each argument will be  added to the Stack in order.  



**Args:**
 
 - <b>`args*`</b>:  arguments must be separated by commas, 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `dequeue`

```python
dequeue()
```

Removes and returns the item at the front of the Queue 

the first item that was added to the queue will be removed and returned. 



**Returns:**
 
 - <b>`"the queue is empty"`</b>:  if the queue instance in empty 

if the queue in not empty, the item at the front of the queue will be returned. 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `enqueue`

```python
enqueue(value)
```

Appends data onto the back of the Queue instance 

the data will be placed in the back of the queue and will be the last to be removed/returned from dequeue() 



**Args:**
 
 - <b>`value`</b>:  data to be pushed onto the queue, can be of any type. 



**Raises:**
 
 - <b>`ValueError`</b>:  if value is null or contains an empty string. 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `front`

```python
front()
```

Return the item at the front of the Queue. 

The first item that was added to the Queue will be returned, and not removed. 



**Returns:**
 
 - <b>`"The queue is empty."`</b>:  if the queue instance is empty. 

if the queue is not empty, the first item added to the queue will be returned 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_queue_id`

```python
get_queue_id()
```

Returns the Queue's instance ID  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_empty`

```python
is_empty()
```

Determines if the Queue is empty 



**Returns:**
 
 - <b>`bool`</b>:  True is the Queue is empty, False otherwise 


---

## <kbd>class</kbd> `Stack`
Stack Class 

A generic stack class that demonstrates last in, first out behavior. 



**Attributes:**
 
 - <b>`Stack.instance_count (int)`</b>:  The number of instantiated stack objects 
 - <b>`_stack_deque`</b> (collections.deque):  The Stack uses an instance of the Deque class 
 - <b>`_stack_id`</b> (int):  The Stack's unique identifier 

<a href="../unit2_stacks_queues/unit2_discussion.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(*args)
```

Initializes a Stack instance 

After each stack initialization, Stack.instance_count is incremented by 1 and the new value is assigned to self._stack_id. Any number of arguments can  be passed into the constructor separated by commas, each argument will be  added to the Stack in order.  



**Args:**
 
 - <b>`args*`</b>:  arguments must be separated by commas, 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_stack_id`

```python
get_stack_id()
```

Returns the Stack instance ID  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_empty`

```python
is_empty()
```

Determines if the Stack is empty 



**Returns:**
 
 - <b>`bool`</b>:  True is the Stack is empty, False otherwise 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `peek`

```python
peek()
```

Return the item at the top of the Stack. 

The last item that was added to the Stack will be returned, and not removed. 



**Returns:**
 
 - <b>`"Peek failed, the stack is empty."`</b>:  if the stack is instance is empty. 

if the stack is not empty, the last item added to the stack will be returned 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `pop`

```python
pop()
```

Removes and reurns the item at the top of the Stack 

the last item that was added to the Stack will be removed and returned. 



**Returns:**
 
 - <b>`"Pop failed, the stack is empty"`</b>:  if the stack instance in empty 

if the stack in not empty, the last item added to the stack will be returned. 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `push`

```python
push(value)
```

Pushes data onto the stack instance 

the data will be placed on the top of the stack and will be the first to be removed/returned from pop() 



**Args:**
 
 - <b>`value`</b>:  data to be pushed onto the stack, can be of any type. 



**Raises:**
 
 - <b>`ValueError`</b>:  if value is null or contains an empty string. 


---

## <kbd>class</kbd> `TodoItem`
A todo item class (real world example) 



**Attributes:**
 
 - <b>`title`</b>:  the title of the todo item 
 - <b>`creation_datetime`</b>:  the date and time the todo item was generated 
 - <b>`completion_datetime`</b>:  the date and time the todo item was completed 

<a href="../unit2_stacks_queues/unit2_discussion.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(title: str)
```

Initializes a todo instance 

After each todo is Initialized, the datetime is saved to creation_datetime. 



**Args:**
 
 - <b>`title`</b>:  the title of the todo instance 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_completion_datetime`

```python
get_completion_datetime()
```

Returns the todo's completion datetime  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L244"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_creation_datetime`

```python
get_creation_datetime()
```

Returns the todo's creation datetime  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_title`

```python
get_title()
```

Returns the todo's title  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reset_completion_datetime`

```python
reset_completion_datetime()
```

resets the completion datetime  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update_completion_datetime`

```python
update_completion_datetime()
```

updates the todo's completion date to the current datetime  




---

## <kbd>class</kbd> `TodoList`
A todo list class, contains todo item objects (real world example) 



**Attributes:**
 
 - <b>`task_queue`</b>:  the todo list's Queue instance, contains non-completed items 
 - <b>`complete_stack`</b>:  Stack instance, contains completed items 

<a href="../unit2_stacks_queues/unit2_discussion.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(*args)
```

Initializes a Todo list 



**Args:**
  args must be strings separated by commas, each arg will be made into Todo  items and added to the task queue 



**Raises:**
 
 - <b>`ValueError`</b>:  if one or more of the args are not strings 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L305"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `add_todo`

```python
add_todo(title: str)
```

Add an item to the todo list 



**Args:**
 
 - <b>`title`</b>:  the title of the new todo task 



**Raises:**
 
 - <b>`ValueError`</b>:  if one or more of the args are not strings 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L319"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `complete_todo`

```python
complete_todo()
```

Removes a todo, updates completion date, then adds it to completed stack 



**Returns:**
 
 - <b>`"todo list is empty"`</b>:  if the todo list is currently empty 

if the task queue is not empty, it will remove the head, add it to the  completed stack, then return the todo's title and completion datetime 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_comleted_length`

```python
get_comleted_length()
```

Returns the length of the complete task stack  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_todo_length`

```python
get_todo_length()
```

Returns the length of task queue  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L337"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `peek_todo`

```python
peek_todo()
```

Returns the title of the next task in the task queue  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L345"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `undo_completion`

```python
undo_completion()
```

Undoes the last task completion 

Removes the todo from the completed stack, resets the completion date, then puts it in the back of the queue 



**Returns:**
 
 - <b>`bool`</b>:  False if stack is empty, True otherwise 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L362"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `view_last_completion`

```python
view_last_completion()
```

Returns a string of the last completed task  






---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
