prompt = "\nZeg iets en ik herhaal het: "
prompt += "\nZeg stop om te stoppen! "
message = ""
while message != 'stop':
    message = input(prompt)
    if message != "stop":
        print(message)
