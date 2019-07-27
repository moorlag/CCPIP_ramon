gastenlijst = ['erik', 'jan', 'karel']
print (gastenlijst)

gast_komt_niet = 'jan'
gastenlijst.remove(gast_komt_niet)
print (gast_komt_niet.title() + " komt niet! ")
print (gastenlijst)

gastenlijst.append('Flora')
print (gastenlijst)

print ('Er komen meer mensen!')
gastenlijst.append("Frans")
gastenlijst.append("Wendy")
gastenlijst.append("jose")
print (gastenlijst)
print ('Balen! De tafel komt te laat')
afvallers = gastenlijst.pop()
print ("Sorry! Ook jij bent niet meer welkom " + afvallers.title())
afvallers = gastenlijst.pop()
print ("Sorry! Ook jij bent niet meer welkom " + afvallers.title())
afvallers = gastenlijst.pop()
print ("Sorry! Ook jij bent niet meer welkom " + afvallers.title())
afvallers = gastenlijst.pop()
print ("Sorry! Ook jij bent niet meer welkom " + afvallers.title())
print (gastenlijst)
del gastenlijst [1]
print (gastenlijst)
del  gastenlijst [0]
print (gastenlijst)
