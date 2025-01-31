deezInputs = input("say something, nerd\n")
stringNuts = "deeznuts"
splitNuts = list(stringNuts)
print("Well why don't you " + deezInputs)
for i in range(len(deezInputs)):
    print(splitNuts[i%8])