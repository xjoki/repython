# format
import math

print('7'.zfill(10))   # 0000000007
print("Schreibe {} und {}".format("Argument1", "Argument2"))
# Schreibe Argument1 und Argument2

print("Schreibe {0} und {1}".format("Argument1", "Argument2"))
# Schreibe Argument1 und Argument2

print("Schreibe {1} und {0}".format("Argument1", "Argument2"))
# Schreibe Argument2 und Argument1

print("Schreibe {Arg1} und {Arg2}".format(Arg1="Argument1", Arg2="Argument2"))

print("PI={}".format(math.pi))      # 3.141592653589793
print("PI={:.4f}".format(math.pi))  # 3.1416

