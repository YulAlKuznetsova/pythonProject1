# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

room = int(input("Введите номер месяца"))
if room == 12 or room == 1 or room == 2:
    print("Зима")
elif 2 < room < 6:
    print("Весна")
elif 5 < room < 9:
    print("Лето")
elif 8 < room < 12:
    print("Осень")
else:
    print("Не номер месяца, введите число от 1 до 12")



number = int(input("Введите номер месяца "))
if number <= 12 and number >= 1:
    mount_dict = {1: "зима",
                  2: "зима",
                  3: "весна",
                  4: "весна",
                  5: "весна",
                  6: "лето",
                  7: "лето",
                  8: "лето",
                  9: "осень",
                  10: "осень",
                  11: "осень",
                  12: "зима"}
    month_list = list(mount_dict.values())
    for i, el in enumerate(month_list):
        if i == number - 1:
            print(f"Время года {month_list[i]}")
else:
    print("Не номер месяца, введите число от 1 до 12")




