import random


#Вопрос №3: Быстрая сортировка

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return quicksort(less) + equal + quicksort(greater)
