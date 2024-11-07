def top_n(items, n):
    """Return the top n items in an array, in desc order

    Args:
        items (array): list or array-like object
        n (int): num of items to return
    Return:
        array: top n items, in desc order
    Egs:
        >>> top_n([8,3,2,7,4],3)
        [8,7,4]
    """

    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[J+1]:
                items[j], items[J+1] = items[j+1], items[j]
    top_n = items[-n:]

    return top_n[::-1]