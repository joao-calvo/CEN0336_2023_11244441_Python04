#!/usr/bin/env python3

# Calculate two cumulative sums, one of all the even values and one of all the odd values.
# Print only the final two sums. The output from your script should be:
# Sum of even numbers: 150
# Sum of odds: 286

lista = [101,2,15,22,95,33,2,27,72,15,52]
sum_par = 0
sum_imp = 0

for numero in lista:
  if (numero % 2 == 0) :
    sum_par = sum_par + numero
  else:
    sum_imp = sum_imp + numero

print ("Sum of even numbers:" , sum_par)
print ("Sum of odds:" , sum_imp)


