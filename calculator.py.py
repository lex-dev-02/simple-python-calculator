zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl): "))
operator = input("operator (+ - * /): ")
ergebnis = (zahl1 + zahl2)
if operator == "+":
    ergebnis = zahl1 + zahl2
elif operator == "-":
    ergebnis = zahl1 - zahl2
elif operator == "*":
    ergebnis = zahl1 * zahl2
elif operator == "/":
    ergebnis = zahl1 / zahl2
print("Dein Ergebnis ist", ergebnis)