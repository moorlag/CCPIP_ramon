prompt = "\nWelke stad ben je geweest:"
prompt += "\nZeg stop als je klaar bent! "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("Dat is een coole stad, " + city.title() + "!")
