#!/usr/bin/env python3
# Print out the length and the sequence, separated by a tab

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for sequencia in lista:
  tamanho = len(sequencia)
  tamanho = str(tamanho)
  print (tamanho + '\t' + sequencia)

