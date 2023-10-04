#!/usr/bin/env python3

# Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.
import sys

inicio = int(sys.argv[1])
final = int(sys.argv[2])

if inicio > final:
  print ( "O primeiro valor deve ser menor que o segundo")

final += 1

while inicio < final:
  print (inicio)
  inicio += 1


