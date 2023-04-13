# text = 'Pierwsza.Druga.Trzecia.Czwarta'
#
# new_text = text.rsplit('.', 1)[1].lower()
# new = text.split('.')
#
# print(new_text)
#
# print(new)
#
# newww = text[::-1]
#
# print(newww)


def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85

func3 = lambda x,y=7:x+y

print(func3(5))
print(func(2))
