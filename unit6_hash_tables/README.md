# Unit 6 Discussion: Dictionaries as Hash Tables

This assignment gave me a good opportunity to think through how a hash map works behind 
the scenes. I did have previous experience with Python dictionaries going to this
assignment, however I had a limited understanding and I assumed these were just lists 
with extra syntax. The challenges that I encountered were mainly trying to understand 
the concept of hash maps from the assignments this week. Taking my time to calculate
the problems from the challenge activities helped me understand the algorithm for 
calculating a key's position and it helped me understand why hash tables are so fast. 

Hash tables utilize a map ADT, which stores data in a key-value pair. Hash tables 
are able to use a key to lookup a value, which allows for data to be retrieved rapidly 
regardless of the size of the hash table. To accomplish this, hash tables store key-value
pairs in an array, using the key to calculate a specific index. However, because there 
is only a finite amount of indices, it is possible for a hash table to calculate the 
same index for two separate keys. This is called a collision, and there are several 
methods to deal with these, such as chaining and probing with open addressing. 
