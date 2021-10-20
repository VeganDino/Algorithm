## Bubble Sort

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for num in reversed(range(len(x))):
        for i in range(num):
            if x[i] > x[i+1]:
                swap(x, i, i+1)