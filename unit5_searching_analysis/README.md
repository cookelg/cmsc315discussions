# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

1. **What concepts or skills did you learn while completing this assignment?**
This was a great opportunity to continue to practice recursion. Additionally, 
implementing a search on a large dataset gave me an opportunity to research and 
learn about memory constraints; I was worried that I would create a list that was 
too large to be contained in memory, and it turns out that a list of ten million 
indices is handled without any issues. It is when the dataset size approaches the 
amount of RAM for the computer the program is running on where this would become an 
issue. Going down this rabbit hole led me to learn how cases like this are handled:
the python libraries Dask and Polars can be used in cases like this.

2. **What challenges did you encounter, and how did you overcome them?**
I initially ran into an issue converting the csv to a list. In my initial attempt,
I simply cast the csv reader object to a list. Instead of strings like I wanted, 
each line of the csv file was cast to its own individual list, giving me a list of 
lists each list containing the email. I instead had to iterate the csv with a for
loop and individually append the strings to the python list. 

3. **Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.**
Linear searches would be more efficient than binary searches in the case of small 
datasets. Linear search is more dynamic than binary search because it can search 
through an unsorted list. For example, if I'm implementing a program that searches 
for employee information for a company that only has a small number of employees, 
or if I am implementing a program that needs to search through an unsorted dataset.
A binary search becomes more useful as the number of objects increases, assuming the
objects in the list are sorted. 
