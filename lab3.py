def non_poslydovny(x):
    for i in range(1, len(x)):
        if abs(x[i] - x[i - 1]) != 1:
            return x[i]
    return None


numbers = [1, 2, 3, 4, 6, 7, 8]
result = non_poslydovny(numbers)
print("Список:", numbers)
print("Непослідовне число:", result)




def non_poslydovny(x):
    for i in range(1, len(x)):
        if abs(x[i] - x[i - 1]) != 1:
            return x[i]
    return None

print("ця програма шукає переше не послідовне число")

text = input("введіть ряд чисел через пробіл, наприклад(1 2 3 4 5 7 8 9):")

numbers = []
for item in text.split():
    numbers.append(int(item))

result = non_poslydovny(numbers)

print("Список:", numbers)

if result is None:
     print("Усі числа послідовні")
else:
     print("Непослідовне число:", result)

a = lambda x: x*x
print(a(5))