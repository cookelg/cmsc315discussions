# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

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
