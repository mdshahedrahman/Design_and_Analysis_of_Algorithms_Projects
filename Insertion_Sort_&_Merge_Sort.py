import random
import time
number_list = [random.randint(0,10000) for i in range(10000)]
#################### Insertion Sort Code ####################
def insertion_sort(array_A):
    for i in range(1, len(array_A)):
        temp = array_A[i]
        j = i-1
        while j >=0 and array_A[j]>temp:
            array_A[j+1]=array_A[j]
            j=j-1
        array_A[j+1]=temp

insertionSort_start_time = time.time()
insertion_sort(number_list)
print(number_list)

insertionSort_end_time = time.time()
insertionSort_execution_time = insertionSort_end_time - insertionSort_start_time
print("Execution time for Insertion sort:", insertionSort_execution_time)

################### Merge Sort Code ####################

import random
import time

number_list = [random.randint(0, 10000) for i in range(10000)]

def mergeSort(array_A):
    if len(array_A) > 1:
        mid_value = len(array_A) // 2
        lower_bound = array_A[:mid_value]
        upper_bound = array_A[mid_value:]

        mergeSort(lower_bound)
        mergeSort(upper_bound)

        i = 0
        j = 0
        k = 0

        while i < len(lower_bound) and j < len(upper_bound):
            if lower_bound[i] <= upper_bound[j]:
                array_A[k] = lower_bound[i]
                i += 1
            else:
                array_A[k] = upper_bound[j]
                j += 1
            k += 1

        while i < len(lower_bound):
            array_A[k] = lower_bound[i]
            i += 1
            k += 1

        while j < len(upper_bound):
            array_A[k] = upper_bound[j]
            j += 1
            k += 1

    return array_A

mergeSort_start_time = time.time()
sorted_list = mergeSort(number_list)
print(sorted_list)
mergeSort_end_time = time.time()

mergeSort_execution_time = mergeSort_end_time - mergeSort_start_time
print("Execution time for Merge sort:", mergeSort_execution_time)
