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

## Data Sctructures

Arrays

- order of operations are simple because calculating an item index s a simple computation and doesn't matter the ammount of items in the array

- Complexity
  - O(1) calculating item index
  - O(n) insertion / deletion of item at the beginning
  - O(n) insertion / deletion of an item in the middle
  - O(1) inserttion / deletion of an item at the end

Linked Lists

- linear colleciton of data elements called nodes
- contain a field pointing to next element in the list along with some data
- first item in the list is the head
- each element has has a filed pointing to the next item in the list
- last item next field is null
- Different types
  - singly - each data item only knows about next neighbor
  - double - each data item knows previous and next data in the list
- fast and easy to add / remove items in list.
- no need to adjust memore
- not possible to do constant time, random access

- Complexity
  - O(n) item lookup
  - O(1) insertion at the front
  - O()
