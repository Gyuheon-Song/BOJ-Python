n, m = map(int, input(). split())

a = set(map(int, input(). split()))
b = set(map(int, input(). split()))

alpha = a-b
beta = b-a

alpha = list(alpha)
beta = list(beta)

print(len(alpha) + len(beta))