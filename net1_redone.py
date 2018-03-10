filename = "data.txt"
noLines = 0

file = open(filename, "r")
for line in file:
    noLines += 1
    l = line.strip('\n')
    L = l.split(" ")
    n = len(L)

syn0 = 2 * random.random((n - 1, noLines)) - 1
syn1 = 2 * random.random((noLines, 1)) - 1