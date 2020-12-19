a, b, c = int(input()), list(map(int, input().split())), list(map(int, input().split()))
print('{0:.1f}'.format(sum([i * j for i, j in zip(b, c)]) / sum(c)))
