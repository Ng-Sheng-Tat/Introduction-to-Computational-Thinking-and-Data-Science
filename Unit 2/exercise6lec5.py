counting = 0
countx_y = 0
for x in range(1, 11):
    for y in range(1, 11):
        counting += 1
        if x > y:
            countx_y += 1

print("Question 1:", counting)
print("Question 2:", "1/" + str(counting))
print("Question 6:", countx_y/counting)

counting2 = 0
allequal = 0

for x in range(1, 9):
    for y in range(1, 9):
        for z in range(1, 9):
            counting2 += 1
            if x == y and y == z:
                allequal += 1

print("Question 7", str(allequal) + "/" + str(counting))



