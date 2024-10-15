# Python program to find a series in an array consisting of characters
"""We are given with an array of char, return True if the sequence of char a, b, c appears in the array somewhere."""

arr = ["f", "x", "a", "i", "c", "t"]


def charCheck(arr):
    for i in range(len(arr) - 2):
        if (arr[i] == "a") and (arr[i + 1] == "b") and (arr[i + 2] == "c"):
            return True
    return False


print(charCheck(arr))