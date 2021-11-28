import sqlalchemy
import psycopg2
import os
from pprint import pprint


def _file_reader(file_name):
    with open(file_name, encoding="utf-8") as f:
        stri = f.readline()
        stri_res = ""
        while stri:
            stri_res = stri_res + stri
            stri = f.readline()
        return stri_res


class Conection:
    def __init__(self):
        self.connection = sqlalchemy.create_engine('postgresql://sqluser:12345@localhost:5432/sqltask_db').connect()

    def incer(self):
        path = os.getcwd() + "\\incertion"
        file_list = os.listdir(path)
        path = path + "\\"
        for file in file_list:
            file_name = path + file
            stri_res = _file_reader(file_name)
            try:
                self.connection.execute(stri_res)
                print(f"{path + file} Успешно загружено")
            except BaseException:  # не знаю какое исключение поставить, здесь должно быть на ошибку уникальности
                print(f"При вставке {path + file} произошла ошибка")

    def select(self):
        print("какой запрос будем выполнять?")
        print("1 - название и год выхода альбомов, вышедших в 2018 году")
        print("2 - название и продолжительность самого длительного трека")
        print("3 - название треков, продолжительность которых не менее 3,5 минуты")
        print("4 - названия сборников, вышедших в период с 2018 по 2020 год включительно")
        print("5 - исполнители, чье имя состоит из 1 слова")
        print('6 - название треков, которые содержат слово "мой"/"my"')
        print('7 - количество исполнителей в каждом жанре')
        print('8 - количество треков, вошедших в альбомы 2019-2020 годов')
        print('9 - средняя продолжительность треков по каждому альбому')
        print('10 - все исполнители, которые не выпустили альбомы в 2020 году')
        #print('11 - названия сборников, в которых присутствует конкретный исполнитель (выберите сами)')
        #print('12 - название альбомов, в которых присутствуют исполнители более 1 жанра')
        #print('13 - наименование треков, которые не входят в сборники')
        #print('14 - исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)')
        #print('15 - название альбомов, содержащих наименьшее количество треков')

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
                case "7":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case "8":
                    path = os.getcwd() + "\\select\\select_songs_in_alboms_year_19_20"
                    break
                case "9":
                    path = os.getcwd() + "\\select\\select_avg_lasting"
                    break
                case "10":
                    path = os.getcwd() + "\\select\\select_realised_not_in_2020"
                    break
                case "11":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case "12":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case "13":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case "14":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case "15":
                    path = os.getcwd() + "\\select\\select_count_group"
                    break
                case _:
                    print("Вы ввели не то!")

        stri_res = _file_reader(path)
        result = self.connection.execute(stri_res).fetchall()
        pprint(result)
