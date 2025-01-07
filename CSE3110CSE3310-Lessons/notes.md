# CSE3110/CSE3310 - Iterative and Recursive Algorithms Notes
## CSE3110 Iterative Algorithms
Iterative Algorithms use loops to process large sets of data.

### Linear Search

Linear search is the easiest to program, but least efficient method of search. It processes the data line by line, similar to how brute force decryption algorithms crack passwords by starting with "a" and attempting every possible combination until "zz..."

```python
FOUND = False
For i in range(len(LIST)):
    if VALUE == LIST[i]:
        FOUND = True
        break
```
Linear search processing time is dependent on the length of the array and the values placement in teh array. Arrays that are 10000 indices or higher can have a noticeable time requirement to process.

### Measuring processing Time
We use ```timer.per_counter()``` to measure the overall time taken between processing data.

For more accurate results, we use the average of at least 30 trials and then use ```statistics.mean()``` to find the average.

### Binary Search
Binary search follows the _divide and conquer_ technique of finding a value. It takes an ordered set of data and tests the midpoint of the set. Then it cuts the list in half and reruns the process.

__Steps for binary Search__
1. Sort the data if unsorted
2. Determine the mid point of the list.
3. Test if the midpoint is the same as the Value?
    * If they're the same, end the program.
4. Is the value larger than the midpoint value?
    * If so, we redefine the lowest value in the set to be one value above the midpoint and re-run the algorithm.
    * Else, redefine the highest value in the range of the list to one value below the midpoint and rerun the algorithm.
5. Repeat 1-4 until the value is found.

* Advantages of Binary Search
    * Significantly faster than linear search
* Disadvantages of Binary Search
    * Must use a sorted list
    * Harder to program

### Sorting Data
Just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort including, bubble, selections, insertion, and merge. (Python uses Timsort, which is a hybrid of merger and insertion osrt designed by Time Peters in 2002).

### Bubble Sort
Bubble  sort compares two adjacent values on the list and arragnes them form lowest to highest. Then it moves to the next index pair and repeats unitl it reaches the end fo the unsorted list.

Advantages are that it is easy to program this algorithm and takes less memory as only two values are tested at a time. However, the disadvantages are that its processing time is directly proportional to the lenght of the data set. Though the set is often fully sorted before the last iteration.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 | 19 |
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 | 19 |
| 1 | 3 | __5__ | 7 | 11 | 13 | 17 | 19 |
| 1 | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |

### Selection Sort
Selection sort compares the curretn index value with the rest of the set. It will find the lowest value in the set and switch position with the lowest index position. As it runs through the data set, it will select the lowest values and place them in the lower positions. Therefore, it sorts the list from head (smallest) to tail (largest).

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | *5* | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | *19* | 13 |
| 1 | 3 | 5 | 7 | __*11*__ | 17 | 19 | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 19 | *17* |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ | *19* |

NOTE: Just like bubble sort, the last column does not need sorting because sorting the second last column will also sor thte last column.

### Insertion Sort
Insertion Sort splites the list into two sections: sorted and unsorted. As it progresses through the list, it takes the left-most value from the unsorted section and isnerts it into the correct location in the section. This algorithm does not scan the entire list each iteration. Instead, the current value needs to only compare with the value immediate to its left.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | _17_ | __19__ | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | 17 | _13_ | __19__ |

* Insertion sort may be faster than selection sort; however, it has more variance depending on how randomized the values in the list are.

For your unit exam, you will need to identify, explain, and compare and contrast various iterative sorts.

# Recursive Algorithms 

A __Recursive Algorithm__ calls itself with smaller or simpler input values. Recursive algorithms have a base case, which reives the simplest input values. This base case is used to stop the recursive portion fo the algorithm. When inputs into a recursive algorithm  are moer complex than the base case, a subprocess will simplyfy the data and re-input the simplfied data into the algorithm again. This process will repeat until the base case is achieved.

All iterative algorithms can be written recursively and vice versa; however, certain functions are easier to write in one form over another.

## Example 1: Testing for the correct input data

```python
# Recursive
def chkInt(VALUE):
    try:
        VALUE = int(VALUE)
        return VALUE
    except ValueError:
        print("You did not enter a number!")
        NEW_VALUE = input("Enter a number: ")
        return chkInt(NEW_VALUE) # recursive return

# Iterative
def chkInt2(VALUE):
    IS_INTEGER = False
    while not IS_INTEGER:
        try:
            VALUE = int(VALUE)
            IS_INTEGER = True
        except ValueError:
            print("You did not enter a number!")
            VALUE = input("Enter a Number: ")
    return VALUE
```


### Iterative vs. Recursive Algorithms
In general, iterative algorithms require more lines of code and more variables than recursive algorithms. They rely on ```while``` and ```for``` loops to complete the process. Whereas, recursive algorithms do not use as many lines and rely on ```return``` values into the function. Recursive algorithms can use more physical memory than iterative algorithms because each instance of the recursive function stays in memory until the base case is reached. Finally, exclusively iterative functions tend to be faster than exclusively recursive functions. However, hybrid iterative and recursive algorithms are fastest.

## Example 2: Factorials 

Calculate 5!

5! = 5 * 4 * 3 * 2 * 1 * 1

BUT!!!!!

4! = 4 * 3 * 2 * 1 * 1

Therefore, we can rewrite 5! as 

5 * 4! = 5 * (4 * 3 * 2 * 1)

Extend this principle,

5! = 5 * (4 * (3 * (2 * (1 * (1)))))

which then can be generalized into 

f(x) = x * (f(x-1)), x > 0

## Recursive Sorting
Recursive sorting uses both recursive and iterative processes. In general, these hybrid sorts are explonentially faster with longer lists. (They are usually measured in a logarithmic scale).

### Merge Sort

Merge sort follows a divide and conquer method of sorting, where the arry is split into its base length and then rebuilt by combining progressively larger _sorted_ lists. The recursive portion is the act of splitting the list into the base case length and the iterative process is the merging of the two smaller sorted lists into one sorted list.

Often times, this function is separated into splitting and merging functions. 

### Quick Sort

Quick Sort (or quicksort) is another divide and conquer method of sorting. Quicksort utilizes an arbitraryvalue as the pivot point. When an iteration compeltes, the pivot value will be placed in its correct position in the list. All other values are compared to the pivot value, swapping values so that all values less than the pivot are on the left and all values greater than the pivot are on the right. The function recuses through each half ot eh array until all values are sorted.


### Heap Sort

Heap sort uses a binary tree organization of an array to sort higher values to the top of the tree. The process of moving larger values higher in the binary tree is called __heapifying__ (or to heapify). When all branches have the largest value as to parent of the heap, the structure is called a __max heap__.

To build the binary tree, each index (starting at 0) will have a left child and right child value (hence, binary tree). The index values can be calculated from the following:

```python
left_child = 2 * parentIndex + 1
right_child = 2 * parentIndex + 2

# sample Tree
LIST = [5, 17, 13, 11, 1, 7, 3]

       5[0]
       /   \
    17[1]   13[2]
    /  \      /  \
  11[3] 1[4] 7[5] 3[6]
```

#### Heapify
To heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom fo the tree and winds its way to the top. If the parent value is smaller than one of the child values, it swaps the parent value with the largest child value. As heapifying mmoves throughout the tree, the higher values will progressively get to the top.

When the heapifying porcess reaches the top, the top value is removed from the tree (and placed at the end of the array). And the value from the highest index (at the bottom of the tree) replaces its position at the top. Then the heapifying process begins again.