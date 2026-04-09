def sameBsts(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        # NOTE: [], [].
        return True
    if len(arrayOne) == 1 and len(arrayTwo) == 1 and arrayOne[0] == arrayTwo[0]:
        # NOTE: [42], [42].
        return True
