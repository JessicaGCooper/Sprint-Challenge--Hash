import itertools

def intersection(arrays):

    nums = list(itertools.chain.from_iterable(arrays))

    index = dict()
    for i in range(len(nums)):
        if nums[i] not in index:
            index[nums[i]] = []

    for array in range(len(arrays)):
        for num in arrays[array]:
            if num in index:
                index[num].append(array)

    result = []

    for number in index:
        if len(index[number]) == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
