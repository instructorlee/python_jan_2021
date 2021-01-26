arr = ["cat", "dog", "horse"]
at = 2
'''
print (
    arr[:at] + arr[at + 1:]
)

arr.pop(2)
print (arr)
'''

# arr.remove('dog')
# arr.pop(1)
del arr[1]
print (arr)