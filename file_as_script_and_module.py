# Datei als Script und importierbares Modul nutzen
def myFunction():
    print("AUSFÜHRUNG")

if __name__ == "__main__":
    from fibo_module import fib_asLst
    print(fib_asLst(1000))
else:
    myFunction()