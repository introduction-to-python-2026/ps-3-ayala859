def approximate_pi(n_terms):
  pi_approximation = 0
  for i in range(n_terms):
    num = 2 * i + 1
    sign = (-1) ** i 
    pi_approximation += sign * (1 / num)
  pi = 4 * pi_approximation
  return pi
