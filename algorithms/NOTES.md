# Algorithm Notes

## Algorithm

- is a set of steps to perform a specific action
- has an associated complexity
    1. space complexity
       - how much memory it requires
    2. time complexity
       - how much time it takes to complete
- has a defined set of inputs and outputs
  - e.g. takes data and puts them into a specific order
- has a classification:
  - serial: work sequentially
  - parallel: breaks up a data into smaller pieces and works on them simultaneously
  - exact / approximate: produces a known predictable value or something close to exact (facial recognition algorithm)
  - deterministic / non-deterministic: executes each step with an exact decision, always produces the same output from a given set of inputs or tries to produce a solution with successive guesses, becoming more accurate over time

## Common Algorithms

Search

- find a specific piece of data within a structure
  
Sorting

- take data and put into some order
  
Computational

- given one set of data, calculate another
  
Collection

- collections of data (i.e. filter out data, count items, etc)

## Writing an algorithm

1. Determine the steps needed to create your algorithm
2. Understand the performance
   1. Measure how an algorithm responds to dataset size
   2. Big O Notation
      - classifies performance as the input size grows
      - "O" indicates the Order of Operation: time slale to perform an operation
      - man algorithms and data sctructures have more than one O value
      - Common Big-O Terms
        1. O(1) - Constant time, e.g. Looking up a single element in an array
        2. O(Log n) - Logarithmic, e.g. Finding an item in a sorted array with binary search
        3. O(n) - Lineary time, e.g. Searching an unsorted array for a specific value
        4. O(n log n) - Log-linear, e.g. Complex sorting algorithms like heap sort and merge sort
        5. O(n^2) - Quadratic, e.g. Simple sorting algorithms, such as bubble sort, selection sort and insertion sort
