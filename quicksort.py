def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          smaller = [i for i in x[1:] if i <= pivot]
          bigger = [i for i in x[1:] if i > pivot]
          return quicksort(smaller) + [pivot] + quicksort(bigger)

print quicksort([10,9,8,7,6,5,4])
print quicksort([1,2,3,4,5,6])
print quicksort([7,2,9,2,4,1])

