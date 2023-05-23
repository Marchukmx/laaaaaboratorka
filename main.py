#3
import random
import logging

def main():
    logging.basicConfig(filename='random.log', level=logging.INFO)

    try:
        count = int(input("Введіть кількість чисел, які потрібно згенерувати: "))
        a = int(input("Введість число для початку діапазону:"))
        b = int(input("Введість число для кінця діапазону:"))
        with open('numbers.txt', 'w') as file:
            for i in range(1, count + 1):
                number = random.randint(a, b)
                file.write(f'{number}\n')
                logging.info(f"Згенеровано число: {number}")

        logging.info(f"Усі числа успішно записано у файл.")

    except ValueError:
        logging.error("Помилка: Некоректний формат кількості чисел.")

    except Exception as e:
        logging.error(f"Сталася помилка: {str(e)}")

main()