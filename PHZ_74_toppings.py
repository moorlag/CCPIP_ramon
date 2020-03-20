prompt = "\nWelke pizza topping wile je: "
prompt += "\nZeg quit als je klaar bent! "
while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print("Nom Nom, " + pizza.title() + " op je Pizza!")
