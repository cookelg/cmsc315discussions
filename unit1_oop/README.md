<!-- markdownlint-disable -->

<a href="../unit1_oop/unit1_discussion.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `unit1_discussion.py`





---

<a href="../unit1_oop/unit1_discussion.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `demonstrate_namespaces`

```python
demonstrate_namespaces()
```






---

<a href="../unit1_oop/unit1_discussion.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `demonstrate_copying`

```python
demonstrate_copying()
```






---

<a href="../unit1_oop/unit1_discussion.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

## <kbd>class</kbd> `ChildClass`
A defensive mage class with a damage reduction ability, extends crawler. 



**Attributes:**
 
 - <b>`name`</b>:  the name of the dungeon crawler 
 - <b>`hit_points`</b>:  the amount of hit points (default 100) 
 - <b>`attack`</b>:  the amount of normal attack damage (default 25) 
 - <b>`is_alive`</b>:  the status of the crawler 
 - <b>`magic_attack`</b>:  the amount of magic attack damage (default 50) 
 - <b>`mana`</b>:  the amount of mana points remaining (default 10) 

<a href="../unit1_oop/unit1_discussion.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(
    name: str,
    hit_points: int = 100,
    attack: int = 25,
    magic_attack: int = 50,
    mana: int = 10
)
```

Create a new defensive mage crawler instance 



**Args:**
 
 - <b>`name`</b>:  the name of the dungeon crawler 
 - <b>`hit_points`</b>:  the amount of hit points (default 100) 
 - <b>`attack`</b>:  the amount of normal attack damage (default 25) 
 - <b>`magic_attack`</b>:  the amount of magic attack damage (default 50) 
 - <b>`mana`</b>:  the amount of mana points remaining (default 10) 




---

<a href="../unit1_oop/unit1_discussion.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `attack`

```python
attack(target)
```

Basic Attack 

Displays the amount of damage dealt and the target's information after each  successful attack. 



**Args:**
 
 - <b>`target`</b>:  another instance of the crawler class 



**Returns:**
 True if the attack is successful, False otherwise. 

---

<a href="../unit1_oop/unit1_discussion.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `deduct_hit_points`

```python
deduct_hit_points(amount)
```

applies a damage reduction to oncoming damage for a mana cost 

Overloaded method from parent class. 



**Args:**
 
 - <b>`amount`</b>:  the amount of damage to be applied 

---

<a href="../unit1_oop/unit1_discussion.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_attack`

```python
get_attack()
```

returns the crawler's attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_hit_points`

```python
get_hit_points()
```

returns the crawler's remaining hit points 

---

<a href="../unit1_oop/unit1_discussion.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_magic_attack`

```python
get_magic_attack()
```

returns the crawler's magic attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_mana`

```python
get_mana()
```

returns the crawler's remaining mana 

---

<a href="../unit1_oop/unit1_discussion.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_name`

```python
get_name()
```

returns the crawler's name 

---

<a href="../unit1_oop/unit1_discussion.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_alive`

```python
is_alive()
```

returns True if the crawler is still alive, False if dead 

---

<a href="../unit1_oop/unit1_discussion.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `magic_attack`

```python
magic_attack(target)
```

The mage crawler's magic attack.  

Can only be used if there is enough remaining mana points. When the attack  is successful, the mana cost is applied to the crawler's remaining mana. 



**Args:**
 
 - <b>`target`</b>:  another instance of the crawler class 



**Returns:**
 True if the attack is successful, False otherwise. 


---

## <kbd>class</kbd> `ParentClass`
A dungeon crawler class 



**Attributes:**
 
 - <b>`name`</b>:  the name of the dungeon crawler 
 - <b>`hit_points`</b>:  the amount of hit points (default 100) 
 - <b>`attack`</b>:  the amount of normal attack damage (default 25) 
 - <b>`is_alive`</b>:  the status of the crawler 

<a href="../unit1_oop/unit1_discussion.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name: str, hit_points: int = 100, attack: int = 25)
```

Create a new dungeon crawler instance 



**Args:**
 
 - <b>`name`</b>:  the name of the dungeon crawler 
 - <b>`hit_points`</b>:  the amount of hit points (default 100) 
 - <b>`attack`</b>:  the amount of normal attack damage (default 25) 




---

<a href="../unit1_oop/unit1_discussion.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `attack`

```python
attack(target)
```

Basic Attack 

Displays the amount of damage dealt and the target's information after each  successful attack. 



**Args:**
 
 - <b>`target`</b>:  another instance of the crawler class 



**Returns:**
 True if the attack is successful, False otherwise. 

---

<a href="../unit1_oop/unit1_discussion.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `deduct_hit_points`

```python
deduct_hit_points(amount)
```

Deduct a specified amount of hit points from the crawler 

 Prints a status update to STDOUT if the crawler dies and changes the   crawler's alive status. 



**Args:**
 
 - <b>`amount`</b>:  the amount of damage to be applied 



**Returns:**
 True if the damage was deducted, False if otherwise 

---

<a href="../unit1_oop/unit1_discussion.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_attack`

```python
get_attack()
```

returns the crawler's attack damage 

---

<a href="../unit1_oop/unit1_discussion.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_hit_points`

```python
get_hit_points()
```

returns the crawler's remaining hit points 

---

<a href="../unit1_oop/unit1_discussion.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_name`

```python
get_name()
```

returns the crawler's name 

---

<a href="../unit1_oop/unit1_discussion.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_alive`

```python
is_alive()
```

returns True if the crawler is still alive, False if dead 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
