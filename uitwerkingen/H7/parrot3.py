prompt = "\nZeg iets en ik herhaal het: "
prompt += "\nZeg stop om te stoppen! "

active = True
while active:
    message = input(prompt)
    if message == 'stop':
        active = False
    else:
        print(message)
