print("hello Prosper, How are you?")
print("what happend?")
# reverse a list in place


def reverse(arr):
    l, r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], [l]
        l, r = l + 1, r - 1
    return arr


print("this is a code that reverses an array") 

