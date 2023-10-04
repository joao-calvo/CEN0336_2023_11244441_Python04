#!/usr/bin/env python3
# Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
indice = 0

for sequencia in lista:
  indice += 1
  tamanho = len(sequencia)
  tamanho = str(tamanho)
  print (indice, "\t",tamanho + '\t' + sequencia)
