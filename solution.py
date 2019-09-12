cleanups = 0
dirtiness = 0
counter = 0
pushes = input()
days = input()
days = days.split(" ")
for i in range(365):
    if dirtiness+counter >= 20:
        dirtiness=0
        cleanups = cleanups + 1
        counter = 0
    for x in range(len(days)):
        if days[x] == str(i+1):
            counter = counter+1
    dirtiness = dirtiness + counter
print(cleanups)