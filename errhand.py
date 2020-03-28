# Error Handling
# Ausnahmen (Exceptions)

while True:
    try:
        x = int(input("Bitte eine Zahl eingeben:"))
        break
    except ValueError:
        print("Ungültige Eingabe!")

# Ausnahme erzwingen mit raise
raise KeyboardInterrupt
