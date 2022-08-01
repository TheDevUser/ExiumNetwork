import os
import termgraph


print(termgraph.shelllogo)

while True:
  shellinput = input(">>> ")
  os.system(shellinput)
