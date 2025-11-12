def approximate_pi(n_terms):
   pi_approximation = 0
   for i in range(n_terms):
      num = ((-1)**i)/(2*i+1)
      pi_approximation += num
   pi = 4 * pi_approximation
   return pi
