#!/usr/bin/env python3

# Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].

lista_tuplas = []
sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC' ]

lista_tuplas = [ (len(i),i) for i in sequencias ] # usando list comprehension

for item in lista_tuplas:
 print (item[0] , "\t" , item [1])

print (lista_tuplas)



