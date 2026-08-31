<!-- markdownlint-disable -->

<a href="../unit3_lists/ArrayList.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ArrayList.py`
### Discussion Board reflection 
1. What concepts or skills did you learn while completing this assignment? This assignment forced me to really focus on what is happening with memory when  a list ADT is at work. It helped me step out of my comfort zone and really see what goes on under the hood for seemingly simple data storing tasks. 

2. What challenges did you encounter, and how did you overcome them? The biggest challenge I ran into with this discussion was attempting to implement a  linked list class. I spun my wheel for a few hours trying to get it to work in Python, but I couldn't figure out how to get Python to allocate a linked list instance  with pointers to null nodes for the head and tail. It seems like when python refers to something as None, it doesn't see it as a placeholder in memory like in Java. I  couldn't figure out how to get this right, so I just moved on to implementing an  ArrayList class. You can review my source code for the linked list class and let  me know what I did wrong. 

3. Linked lists and array list ADT's can affect real-world applications in different ways depending on their use case. For example, a linked list will be able to populate new data a lot more efficiently because adding a new data item to an existing list  only requires two pointers to be updated. On the other hand, an array list ADT might  have to iterate through and shift a large number of existing items to make room. The array list makes up for this by allowing for efficient sorting algorithms that a  linked list cannot support. 



---

## <kbd>class</kbd> `ArrayList`
An Array list class 



**Attributes:**
 
 - <b>`alloc_size`</b> (int):  the total number of allocations for the list 
 - <b>`length`</b> (int):  the total number of items in the list 
 - <b>`_arr`</b> (list):  the Python list that contains the items 

<a href="../unit3_lists/ArrayList.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(start_size: int) → None
```

Initializes an ArrayList instance 

The ArrayList is initialized with a length of zero, and the number of allocated spaces is given as an argument 



**Attributes:**
 
 - <b>`start_size`</b> (int):  the starting number of allocations in the list 




---

<a href="../unit3_lists/ArrayList.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `append`

```python
append(data)
```

Appends data to the end of the list 

If the length of the list is as long as alloc_size, the allocation is doubled 



**Attributes:**
 
 - <b>`data`</b>:  the item to be added to the list 

---

<a href="../unit3_lists/ArrayList.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `insert_at`

```python
insert_at(index: int, data)
```

Inserts data to a specified index 

If the length of the list is as long as alloc_size, the allocation is doubled 



**Attributes:**
 
 - <b>`index`</b> (int):  the index at which the data will be added 
 - <b>`data`</b>:  the data to be added to the ArrayList 

---

<a href="../unit3_lists/ArrayList.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `prepend`

```python
prepend(data)
```

Prepends data to the beginning of the list 

If the length of the list is as long as alloc_size, the allocation is doubled 



**Attributes:**
 
 - <b>`data`</b>:  the item to be added to the list 

---

<a href="../unit3_lists/ArrayList.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `remove_at`

```python
remove_at(index: int)
```

Removes data from a specified index 



**Attributes:**
 
 - <b>`index`</b> (int):  the index from which data will be removed 

**Returns:**
 returns the item removed from the ArrayList 

**Raises:**
 
 - <b>`ValueError`</b>:  if the index argument is beyond the range of the ArrayList 

---

<a href="../unit3_lists/ArrayList.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `resize`

```python
resize(new_alloc_size: int)
```

Adds additional allocations to the ArrayList 



**Attributes:**
 
 - <b>`new_alloc_size`</b> (int):  the new allocation size of the ArrayList 

---

<a href="../unit3_lists/ArrayList.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `search`

```python
search(item)
```

Searches the ArrayList for the provided argument 

**Attributes:**
 
 - <b>`item`</b>:  the data to be searched for 

**Returns:**
 If the item exists, returns the index of the item If the item does not exist, returns -1 

**Raises:**
 
 - <b>`ValueError`</b>:  if the index argmument is beyond the range of the ArrayList 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
