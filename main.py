def main():

    logging.basicConfig(filename='abaza.log', level=logging.INFO)

    try:
        name = input("Введіть ваше ім'я: ")
        age = int(input("Введіть ваш вік: "))

        with open('data.txt', 'w') as file:
            file.write(f'Ім\'я: {name}\n')
            file.write(f'Вік: {age}\n')

        logging.info("Дані успішно записано у файл.")

    except ValueError:
        logging.error("Помилка: Некоректний формат даних.")

    except Exception as e:
        logging.error(f"Сталася помилка: {str(e)}")

if __name__ == '__main__':
    main()