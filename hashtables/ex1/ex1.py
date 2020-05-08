weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]

def get_indices_of_item_weights(weights, length, limit):

    w = dict() 
    
    for i in range(length):
        if weights[i] not in w:
            w[weights[i]] = i
        else:
            w[weights[i]] = (i, w[weights[i]])

    for weight, index in w.items():
        paired_weight = limit - weight
        if paired_weight in w:
            if w[paired_weight] > index:
                return (w[paired_weight], index)
            elif index > w[paired_weight]:
                return (index, w[paired_weight])
            elif weight == paired_weight:
                return index
            else:
                return None

    """
    YOUR CODE HERE
    """


print(get_indices_of_item_weights(weights, 9, 7))

