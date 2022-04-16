

check = 30
if check < 0:
    print("It is <0")
elif check >= 0 and check <= 10:
    print("It is in [0,10]")
else:
    print("It is >10")


numbers = [1, 2, 3, 4, 5]
names = ["Nick", "SonZai", "Slava"]
for item in numbers:
    print(item)
for item in names:
    print(item)


run = True
current = 1
finish = 532
while run:
    if current > finish:
        run = False
    else:
        current += 25
        print("Current is", current)


# Cool regex
import re


str = "\"I AM NO YELLING\", she said. Though we knew it to not be true."
new_str = re.sub("[,.\'\"A-Z+' ']", "_", str)
last_str = str + "6 298 - 345"
print(str)
print(new_str)
print(last_str)
new_str = re.sub('[^0-9]', '_', last_str)
print(new_str)
