# Kreisberechnung
import math

radius = input("Radius in cm? : ")
radius = float(radius)

umfang = (2 * math.pi) * radius
flaeche = (math.pi * radius) * radius

print("Kreisumfang : {:.2f} cm".format(umfang))
print("Kreisfläche : {:.2f} cm²".format(flaeche))
