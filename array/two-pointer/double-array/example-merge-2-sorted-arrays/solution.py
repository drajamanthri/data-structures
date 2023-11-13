
def merge (a1: list, a2:list)->list:
    i = 0
    j = 0
    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1

    while i < len(a1):
        result.append(a1[i])
        i += 1

    while j < len(a2):
        result.append(a2[j])
        j += 1

    return result

a1 = [1, 4, 6, 7, 20]
a2 = [3, 5, 6]
print (merge(a1, a2))

