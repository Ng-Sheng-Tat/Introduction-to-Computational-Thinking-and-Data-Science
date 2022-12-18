counting = 0
iseven = 0
condx_y = 0
x_or_y = 0

for x in range(1, 5):
    for y in range(1, 5):
        counting += 1
        if (x + y) % 2 == 0:
            iseven += 1
        if x > y:
            condx_y += 1
        if x == 4 or y == 4:
            x_or_y += 1

print(iseven/counting)
print(condx_y/counting)
print(x_or_y/counting)