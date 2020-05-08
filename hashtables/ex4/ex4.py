def has_negatives(a):

    no_negatives = []
    for each in a:
        no_negatives.append(abs(each))
    
    check = dict()
    for num in no_negatives:
        if num not in check:
            check[num] = 1
        else:
            check[num] += 1
    result = []
    for num, count in check.items():
        if count > 1:
            result.append(num)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
