def productSum(array):
    return recurse_product_sum(array, factor=1, summation=0)


def recurse_product_sum(array, factor, summation):
    for el in array:
        if isinstance(el, list):
            recursed_summation = recurse_product_sum(el, factor=factor + 1, summation=0)
            summation += recursed_summation
        else:
            summation += el
    return factor * summation
