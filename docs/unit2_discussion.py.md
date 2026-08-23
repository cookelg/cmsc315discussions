<!-- markdownlint-disable -->

<a href="../unit2_stacks_queues/unit2_discussion.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `unit2_discussion.py`
=========================================================== UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON) =========================================================== 

OVERVIEW: This assignment introduces two fundamental data structures: the Stack (LIFO) and the Queue (FIFO). 

You will complete, modify, and extend the starter code while explaining key concepts through comments and improved output. 

**Global Variables**
---------------
- **stack1**
- **queue1**

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(*args)
```

Initializes a Queue instance 

After each queue initialization, Queue.instance_count is incremented by 1 and the new value is assigned to self._queue_id. Any number of arguments can  be passed into the constructor separated by commas, each argument will be  added to the Stack in order.  



**Args:**
 
 - <b>`args*`</b>:  arguments must be separated by commas, 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_queue_id`

```python
get_queue_id()
```

Returns the Queue's instance ID  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(*args)
```

Initializes a Stack instance 

After each stack initialization, Stack.instance_count is incremented by 1 and the new value is assigned to self._stack_id. Any number of arguments can  be passed into the constructor separated by commas, each argument will be  added to the Stack in order.  



**Args:**
 
 - <b>`args*`</b>:  arguments must be separated by commas, 




---

<a href="../unit2_stacks_queues/unit2_discussion.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_stack_id`

```python
get_stack_id()
```

Returns the Stack instance ID  



---

<a href="../unit2_stacks_queues/unit2_discussion.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_empty`

```python
is_empty()
```

Determines if the Stack is empty 



**Returns:**
 
 - <b>`bool`</b>:  True is the Stack is empty, False otherwise 

---

<a href="../unit2_stacks_queues/unit2_discussion.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../unit2_stacks_queues/unit2_discussion.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
