__Date__ = '9/23/2015'


def insertion_sort(array_to_sort):
    for j in range(1, len(array_to_sort)):
        key = array_to_sort[j]
        i = j - 1
        while (i >=0) and (array_to_sort[i] > key):
            array_to_sort[i+1] = array_to_sort[i]
            i -= 1
        array_to_sort[i+1] = key


x = [2,7,3,8,1]
insertion_sort(x)
print(x)