<!-- markdownlint-disable -->

<a href="../unit1_oop/unit1_discussion.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `unit1_discussion.py`
=========================================================== Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying =========================================================== 

INSTRUCTIONS: In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python. You are provided with starter code containing TODO sections. Your task is to complete, modify, and analyze the code to demonstrate understanding of inheritance, namespaces, and object copying. 


---

<a href="../unit1_oop/unit1_discussion.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `demonstrate_namespaces`

```python
demonstrate_namespaces()
```






---

<a href="../unit1_oop/unit1_discussion.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `demonstrate_copying`

```python
demonstrate_copying()
```






---

<a href="../unit1_oop/unit1_discussion.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

## <kbd>class</kbd> `ChildClass`
A defensive mage class with a damage reduction ability, extends crawler 

<a href="../unit1_oop/unit1_discussion.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name, hit_points=100, attack=25, magic_attack=50, mana=10)
```

Create a new defensive mage crawler instance 

the mage's alive status is set to True when instantiated. 

name            the name of the dungeon crawler hit_points      the amount of hit points (default 100) attack          the amount of normal attack damage (default 25) magic_attack    the amount of magic attack damage (default 50) mana            the amount of mana points remaining (default 10) 




---

<a href="../unit1_oop/unit1_discussion.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `attack`

```python
attack(target)
```

Attack another crawler 

Displays the amount of damage dealt and the target's information after each  successful attack. 

Return True if the attack was successful, False if the crawler is currently dead, False if the target is already dead. 

---

<a href="../unit1_oop/unit1_discussion.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `deduct_hit_points`

```python
deduct_hit_points(amount)
```

Overloaded method from parent class applies a damage reduction to oncoming damage for a mana cost 

---

<a href="../unit1_oop/unit1_discussion.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_attack`

```python
get_attack()
```

returns the crawler's attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_hit_points`

```python
get_hit_points()
```

returns the crawler's remaining hit points 

---

<a href="../unit1_oop/unit1_discussion.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_magic_attack`

```python
get_magic_attack()
```

returns the crawler's magic attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_mana`

```python
get_mana()
```

returns the crawler's remaining mana 

---

<a href="../unit1_oop/unit1_discussion.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_name`

```python
get_name()
```

returns the crawler's name 

---

<a href="../unit1_oop/unit1_discussion.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_alive`

```python
is_alive()
```

returns True if the crawler is still alive, False if dead 

---

<a href="../unit1_oop/unit1_discussion.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `magic_attack`

```python
magic_attack(target)
```

The mage crawler's magic attack, can only be used if there is enough remaining mana points. When the attack is successful, the mana cost is  applied to the crawler's remaining mana and returns True. Returns False if insufficient mana points. 


---

## <kbd>class</kbd> `ParentClass`
A dungeon crawler class 

<a href="../unit1_oop/unit1_discussion.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name, hit_points=100, attack=25)
```

Create a new dungeon crawler instance. 

the player's alive status is set to True when instantiated. 

name        the name of the dungeon crawler hit_points  the amount of hit points (default 100) attack      the amount of normal attack damage (default 25) 




---

<a href="../unit1_oop/unit1_discussion.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `attack`

```python
attack(target)
```

Attack another crawler 

Displays the amount of damage dealt and the target's information after each  successful attack. 

Return True if the attack was successful, False if the crawler is currently dead, False if the target is already dead. 

---

<a href="../unit1_oop/unit1_discussion.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `deduct_hit_points`

```python
deduct_hit_points(amount)
```

deduct a specified amount of hit points from the crawler 

Returns True if the damage was deducted, Prints a status update to STDOUT if the crawler dies and changes the crawler's slive status. 

Returns False if the crawler is already dead. 

---

<a href="../unit1_oop/unit1_discussion.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_attack`

```python
get_attack()
```

returns the crawler's attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_hit_points`

```python
get_hit_points()
```

returns the crawler's remaining hit points 

---

<a href="../unit1_oop/unit1_discussion.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_name`

```python
get_name()
```

returns the crawler's name 

---

<a href="../unit1_oop/unit1_discussion.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_alive`

```python
is_alive()
```

returns True if the crawler is still alive, False if dead 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
