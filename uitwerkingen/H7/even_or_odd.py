nummer = input("Met deze controle laat ik zien dat ik het verschil weet tussen even en oneven getallen. Geef getal: ")
nummer = int(nummer)
if nummer % 2 == 0:
    print("Het getal is.... " + str(nummer) + " even!")
else:
    print("Het getal is.... " + str(nummer) + " oneven!")
