# NOTE: A brute force approach.
# class AncestralTree:
#     def __init__(self, name):
#         self.name = name
#         self.ancestor = None
#
#
# def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
#     # NOTE:
#     # path one: A B E.
#     # path two: A B D I.
#
#     descendant_one_path = []
#     while descendantOne is not None:
#         descendant_one_path.append(descendantOne)
#         descendantOne = descendantOne.ancestor
#     descendant_one_path.reverse()
#
#     descendant_two_path = []
#     while descendantTwo is not None:
#         descendant_two_path.append(descendantTwo)
#         descendantTwo = descendantTwo.ancestor
#     descendant_two_path.reverse()
#
#     youngest_common_ancestor = None
#
#     for one_ancestor in descendant_one_path:
#         for two_ancestor in descendant_two_path:
#             if one_ancestor.name == two_ancestor.name:
#                 youngest_common_ancestor = one_ancestor
#
#     return youngest_common_ancestor


# NOTE: A hash set approach.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    history = set()

    while descendantOne is not None:
        history.add(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo is not None:
        if descendantTwo in history:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor
