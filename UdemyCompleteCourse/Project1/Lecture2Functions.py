

print("日本語を勉強してばかりいる。")
print("上手になれように練習する。")


def print_some_cool_stuff(str1, str2):
    print(str1)
    print(str2)


print_some_cool_stuff("髪をとかす。", "神を切る。")
print_some_cool_stuff("中国語が面白い。", "神を切る。")


def print_name_and_age(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


# = key arguments
print_name_and_age("Slava", 20)
print_name_and_age("SonZai")
print_name_and_age(age=27)


# * creates array
def print_infinite_people(*people):
    for person in people:
        print("This person is", person)


print_infinite_people("Nick", "Dan", "Slava", "SonZai")


def do_math(num1, num2):
    return num1 + num2


math1 = do_math(5, 7)
math2 = do_math(math1, 12)
print("THe first sum is", math1, "and the second sum is", math2)
