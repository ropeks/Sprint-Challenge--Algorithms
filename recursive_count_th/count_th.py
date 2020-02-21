'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case: if the word len is less or equal to 1
    if len(word) <= 1:
        return 0
    # check first two letters
    if word[:2] == 'th':
        # return 1 plus recursion of the word minus first two letters
        return 1 + count_th(word[2:])
    # skip the first letter and continue with recursion
    else:
        return count_th(word[1:])
