# Sorting

Welcome to my sorting exercise.

The four algorithms visualized are: bubble sort, heap sort, merge sort, and last but possibly the least (time required), quicksort.

The four algorithms are different in efficiency but the clock rates are calibrated so that they appear to reach a sorted array in roughly the same amount of time for better viewing pleasure. At the same time, the advantage of the latter two algorithms should be easily noticeable.

## Bubble Sort

<b>Bubble sort</b> is a simple process of repeatedly going through the array and compare the two adjacent elements, and switching them if they're in the wrong order, i.e. the left element is greater than the right element. It's not particularly efficient on a large scale but is nevertheless fun to watch.

![](https://github.com/tianxiaozhang1/sorting/blob/main/bubble.gif)

## Heapsort

<b>Heapsort</b> is essentially two steps. One is to build a heap in the form of a binary tree. Two is to constantly remove the largest number element and adding it to the array. The heap is updated from each removal.

![](https://github.com/tianxiaozhang1/sorting/blob/main/heap.gif)

## Merge Sort

<b>Merge sort</b> is a divide-and-conquer algorithm, invented by (THE) John von Neumann in 1945. It divides the sequence in half until the two halves are both one element in length. Sublists are then merged back together to produce a longer list until there's only one sublist left (with the same length as the original array), which is sorted.

![](https://github.com/tianxiaozhang1/sorting/blob/main/merge.gif)

## Quicksort

<b>Quicksort</b> is another divide-and-conquer algorithm, invented by Tony Hoare in 1959. An arbitrary element is selected (initial element in this case) and all remaining elements in the current array are compared to it, and the ones smaller will be moved to its left and the ones greater will remain on the right. The initial element is now a pivot and its position in the final sequence is known since everything smaller than it is to its left, and all greater elements on the right. The array is then divided into two with the pivot removed in the middle. The process continues until the entire original array is finished.

![](https://github.com/tianxiaozhang1/sorting/blob/main/quick.gif)

## Personal note

The two divide-and-conquer algorithms (merge sort and quicksort) are particularly interesting (and difficult) to visualize because divide-and-conquer intentionally works on a small section at a time (hence the efficiency) and visualization requires the full picture to be maintained at all times. The scale here isn't significant enough but it would be fun to see how much the visualization slows down the calculation process and how much edge the otherwise-efficient algorithms would still have over the first two less efficient algorithms (especially bubble sort) when the array is much larger.

## Further reading

https://users.cs.duke.edu/~ola/bubble/bubble.html

https://cs50.harvard.edu/ap/2020/assets/pdfs/bubble_sort.pdf

http://personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/heapSort.htm

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf

https://algs4.cs.princeton.edu/22mergesort/

https://algs4.cs.princeton.edu/lectures/keynote/22Mergesort.pdf

https://algs4.cs.princeton.edu/23quicksort/

And these videos are very well worth a watch:

https://www.youtube.com/watch?v=TZRWRjq2CAg

https://www.youtube.com/watch?v=H5kAcmGOn4Q

https://www.youtube.com/watch?v=es2T6KY45cA

https://www.youtube.com/watch?v=aXXWXz5rF64

Thanks for visiting.
