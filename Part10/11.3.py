import set as data


def cmp(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    return -1


def insertion_sort(arr, left, right, cmp_func=cmp):
    for i in range(left + 1, right + 1):
        item = arr[i]
        j = i
        while cmp_func(j, left) + cmp_func(arr[j-1], item) == 2:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = item
    return arr


if __name__ == "__main__":
    n = 5
    data_array = data.unsortedArr(n)
    print("\nrandom array: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.nearlySortedArr(n)
    print("\nalmost sorted: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.reversedNSA(n)
    print("\nreversed almost sorted : ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.gaussian(n)
    print("\nrandom gaussian: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.arrK_set(n)
    print("\nrandom k set: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))
