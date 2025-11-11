def approximate_pi(n_terms):
  total = 0
  for i in range(n_terms):
    num = 2 * i + 1
    sign = (-1) ** i 
    total += sign * (1 / num)
  pi = 4 * total
  return pi
n_terms = 1000
result = approximate_pi(n_terms)
print(result)
