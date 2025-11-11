def approximate_pi(n_terms):
  for i in range(1,n_terms):
    num = 2 * i + 1
    sign = (-1) ** i 
    term = sign * (1/num) 
    leibni_series.append(term)
  pi = 4 * (sum(leibni_series))
  return pi
