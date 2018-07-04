try:
    a = 4
    b = a/0
    f = open('ac.txt')
    for line in f:
        print(line)
except FileNotFoundError as e:
    print(e.filename)
except Exception as e:
    print(e)

#i = 0/0