#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата рождения (список из трёх чисел).
# Написать программу, выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по датам рождения; вывод на экран информацию о людях, родившихся под знаком, название которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение. Оформив каждую команду в виде отдельной функции.
# Добавьте возможность хранения файла данных в домашнем каталоге пользователя.
# Для выполнения операций с файлами необходимо использовать модуль pathlib .

import pathlib
import json
import os

data_file = pathlib.Path.home() / "data.json"

def read_data():
    if data_file.exists():
        with open(data_file, "r") as file:
            data = json.load(file)
        return data
    else:
        return []

def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)


def input_data():
    data = []
    while True:
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        zodiac = input("Введите знак Зодиака: ")
        birthday = input("Введите дату рождения (через пробел): ").split()
        if len(birthday) != 3:
            print("Неверный формат даты. Повторите ввод.")
            continue
        try:
            birthday = [int(x) for x in birthday]
        except ValueError:
            print("Неверный формат даты. Повторите ввод.")
            continue
        data.append({
            "фамилия": surname,
            "имя": name,
            "знак Зодиака": zodiac,
            "дата рождения": birthday
        })
        if input("Желаете добавить еще запись? (y/n): ") != 'y':
            break
    data.sort(key=lambda x: x["дата рождения"])
    return data


def find_people_by_zodiac(data, zodiac):
    people = []
    for person in data:
        if person["знак Зодиака"] == zodiac:
            people.append(person)
    return people


def print_people(people):
    if len(people) == 0:
        print("Нет людей с таким знаком Зодиака.")
    else:
        for person in people:
            print("Фамилия: {}".format(person["фамилия"]))
            print("Имя: {}".format(person["имя"]))
            print("Знак Зодиака: {}".format(person["знак Зодиака"]))
            print("Дата рождения: {}/{}/{}".format(person["дата рождения"][0], person["дата рождения"][1],
                                                   person["дата рождения"][2]))
            print()


def main():
    filename = os.environ.get("DATA_FILE")
    if filename:
        with open(filename, "r") as file:
            data = eval(file.read())
    else:
        data = input_data()

    zodiac = input("Введите знак Зодиака для поиска: ")
    people = find_people_by_zodiac(data, zodiac)
    print_people(people)


if __name__ == "__main__":
    main()







