#!/usr/bin/env python3

# Save the string sapiens, erectus, neanderthalensis as a variable named taxa.
taxa = 'sapiens, erectus, neanderthalensis'

# Print taxa.
print (taxa)

# Print taxa[1], what do you get?
print (taxa[1])

# Print type(taxa). What is it's type?
print (type(taxa))

# Split taxa into individual words and print the result of the split. (Think about the ',')
# Store the result of split in a new variable named species.
# Print species.
species = taxa.split(',')
print (species)

# Print the species[1], What do you get?
print (species[1])

# Print type(species). What is it's type?
print (type(species))

# Sort the list alphabetically and print (hint: lookup the function sorted()
lista_ordenada = sorted(species)
print ("Lista em ordem alfabetica:" , lista_ordenada)

# Sort the list by length of each string and print. (The shortest string should be first). 
lista_tamanho = sorted(species, key=len)
print ("Lista ordenada por comprimento:" , lista_tamanho)
