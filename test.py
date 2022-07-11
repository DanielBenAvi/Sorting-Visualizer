import random

randomlist = random.sample(range(1, 21), 20)
for i in range(len(randomlist)):
    for j in range(len(randomlist)):
        if randomlist[i] < randomlist[j]:
            temp = randomlist[i]
            randomlist[i] = randomlist[j]
            randomlist[j] = temp
            print(randomlist)

        
print(randomlist)


def is_sorted(lst) -> bool:
    for i in range(len(lst)-1):
        if (lst[i]>lst[i+1]):
            return False
    return True

print(is_sorted(randomlist))