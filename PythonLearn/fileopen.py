def openf():
    pathr="d:\\1.txt"
    with open(pathr,"r+") as f:
        print(f.read())
        f.write('Hello, world111!')