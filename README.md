# Problem Definition
We are given an unsorted array A[1...n]. Now, imagine its sorted version. The unsorted array has the property that each element has a distance of at most k positions, where 0<k<=n, from its index in the sorted version. For example, when k is 2, an element at index 5 in the sorted array, can be at one of the indices {3,4,5,6,7} in the unsorted array. 

# Possible Solution
The unsorted array can be sorted efficiently by utilizing a Min-Heap data structure.
-Create a Min Heap of size k+1 with first k+1 elements,
-One by one remove min element from the heap, put it in the result array, and add a new element to the heap from remaining elements.

# Libraries & Dependencies
Numpy

Matplotlib.pyplot

Time

Random


# Runtimes Comparison
![Ekran Görüntüsü (545)](https://user-images.githubusercontent.com/58219688/146238248-6636853b-a7e9-4dba-a26b-a19889e66392.png)

![Ekran Görüntüsü (544)](https://user-images.githubusercontent.com/58219688/146238271-1936e769-d3fe-4b76-a297-c14da90a3232.png)


As seen in the figures above, runtimes are pretty much the same. However, they can be different in some cases and it is because this program examined in this very file is based on “random” arrays. In some cases, one of them can be better than the other (e.g . in cases where the array is reverse sorted or randomly picked bad pivot etc, quick sort goes n^2)
