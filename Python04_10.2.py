#!/usr/bin/env python3

# Modify your script so that it will only print the number if it is odd.
import sys

inicio = int(sys.argv[1])
final = int(sys.argv[2])

if inicio > final:
  print ( "O primeiro valor deve ser menor que o segundo")

final += 1

while inicio < final:
 if inicio % 2 != 0:
  print (inicio)
 inicio += 1


