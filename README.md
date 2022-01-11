# Objective

This repository aims to document my studies in software engineering based on [coding interview university](https://github.com/jwasham/coding-interview-university) and other sources. 

# Study Plan

- [Algorithmic complexity / Big-O / Asymptotic analysis](#algorithmic-complexity--big-o--asymptotic-analysis)
- [Data Structures](#data-structures)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stack](#stack)
    - [Queue](#queue)
    - [Hash table](#hash-table)

## Algorithmic complexity / Big-O / Asymptotic analysis

- Nothing to implement here, you're just watching videos and taking notes! Yay!
- There are a lot of videos here. Just watch enough until you understand it. You can always come back and review.
- Don't worry if you don't understand all the math behind it.
- You just need to understand how to express the complexity of an algorithm in terms of Big-O.
- [X] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [X] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [X] [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [X] Skiena:
    - [video](https://www.youtube.com/watch?v=gSyDMtdPNpU&index=2&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [slides](https://archive.org/details/lecture2_202008)
- [X] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [X] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [X] TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
    - [Computational Complexity: Section 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)
- [X] [Cheat sheet](http://bigocheatsheet.com/)


## Data Structures

- ### Arrays
    - [ ] About Arrays:
        - [Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)
        - [UCBerkley CS61B - Linear and Multi-Dim Arrays (video)](https://youtu.be/Wp8oiO_CZZE?t=15m32s)
        - [Basic Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_04-basicArrays.mp4)
        - [Multi-dim (video)](https://archive.org/details/0102WhatYouShouldKnow/02_05-multidimensionalArrays.mp4)
        - [Dynamic Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/EwbnV/dynamic-arrays)
        - [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
        - [Jagged Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_06-jaggedArrays.mp4)
        - [Resizing arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/03_01-resizableArrays.mp4)
    - [ ] Implement a vector (mutable array with automatic resizing):
        - [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
        - [ ] New raw data array with allocated memory
            - can allocate int array under the hood, just not use its features
            - start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
        - [ ] size() - number of items
        - [ ] capacity() - number of items it can hold
        - [ ] is_empty()
        - [ ] at(index) - returns item at given index, blows up if index out of bounds
        - [ ] push(item)
        - [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
        - [ ] prepend(item) - can use insert above at index 0
        - [ ] pop() - remove from end, return value
        - [ ] delete(index) - delete item at index, shifting all trailing elements left
        - [ ] remove(item) - looks for value and removes index holding it (even if in multiple places)
        - [ ] find(item) - looks for value and returns first index with that value, -1 if not found
        - [ ] resize(new_capacity) // private function
            - when you reach capacity, resize to double the size
            - when popping an item, if size is 1/4 of capacity, resize to half
    - [ ] Time
        - O(1) to add/remove at end (amortized for allocations for more space), index, or update
        - O(n) to insert/remove elsewhere
    - [ ] Space
        - contiguous in memory, so proximity helps performance
        - space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)