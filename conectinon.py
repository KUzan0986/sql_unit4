import sqlalchemy
import psycopg2
import os

class Conection:
    def __init__(self):
        self.connection = sqlalchemy.create_engine('postgresql://sqluser:12345@localhost:5432/sqltask_db').connect()

    def incer(self):

        path = os.getcwd() + "\\incertion"
        file_list = os.listdir(path)
        path = path + "\\"
        for file in file_list:
            file_name = path + file
            with open(file_name, encoding="utf-8") as f:
                stri = f.readline()
                stri_res = ""
                while stri:
                    stri_res = stri_res + stri
                    stri = f.readline()
            try:
                self.connection.execute(stri_res)
                print(f"{path + file} Успешно загружено")
            except BaseException: #не знаю какое исключение поставить, здесь должно быть на ошибку уникальности
                print(f"При вставке {path + file} произошла ошибка")

    def select(self):
        print("какой запрос будем выполнять?")
        print("1 - название и год выхода альбомов, вышедших в 2018 году")
        print("2 - название и продолжительность самого длительного трека")
        print("3 - название треков, продолжительность которых не менее 3,5 минуты")
        print("4 - названия сборников, вышедших в период с 2018 по 2020 год включительно")
        print("5 - исполнители, чье имя состоит из 1 слова")
        print('6 - название треков, которые содержат слово "мой"/"my"')
        while True:
            сheck = input("введите число")
            match сheck:
                case "1":
                    path = os.getcwd() + "\\select\\select_albom_2018"
                    break
                case "2":
                    path = os.getcwd() + "\\select\\select_max_lasting"
                    break
                case "3":
                    path = os.getcwd() + "\\select\\select_lastin_more_210"
                    break
                case "4":
                    path = os.getcwd() + "\\select\\selection_collectons_2018_2020"
                    break
                case "5":
                    path = os.getcwd() + "\\select\\select_one_name"
                    break
                case "6":
                    path = os.getcwd() + "\\select\\select_my"
                    break
                case _:
                    print("Вы ввели не то!")

        with open(path, encoding="utf-8") as f:
            result = self.connection.execute(f.readline()).fetchall()
        print(result)
#connection.execute("SELECT * FROM database;").fetchmany(10)