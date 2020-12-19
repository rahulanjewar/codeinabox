from math import sqrt
n, ar = int(input()), list(map(int, input().split()))
print(sqrt(sum([(i - (sum(ar) / n)) ** 2 for i in ar]) / n))
