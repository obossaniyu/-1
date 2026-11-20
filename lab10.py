
import json
from datetime import datetime


class Schedule:
    def __init__(self):
        self.lessons = {}

    def check_conflict(self, day, start, end, room, exclude=None):
        """Проверка конфликтов занятий."""
        for name, lesson in self.lessons.items():
            if name == exclude:
                continue

            if lesson["day"].lower() == day.lower():
                if start < lesson["end"] and end > lesson["start"]:
                    if lesson["room"] == room:
                        raise ValueError("Аудитория уже занята")

                    raise ValueError("Конфликт времени занятий")

    def validate(self, name, day, start, end, room):
        """Проверка входных данных."""
        if not name.strip() or not room.strip():
            raise ValueError("Название и аудитория обязательны")

        days = [
            "понедельник", "вторник", "среда",
            "четверг", "пятница", "суббота",
            "воскресенье"
        ]

        if day.lower() not in days:
            raise ValueError("Некорректный день недели")

        start = datetime.strptime(start, "%H:%M").strftime("%H:%M")
        end = datetime.strptime(end, "%H:%M").strftime("%H:%M")

        if start >= end:
            raise ValueError("Некорректное время занятия")

        return start, end

    def add(self, name, day, start, end, room):
        """Добавление занятия."""
        if name in self.lessons:
            raise ValueError("Занятие уже существует")

        start, end = self.validate(name, day, start, end, room)
        self.check_conflict(day, start, end, room)

        self.lessons[name] = {
            "day": day,
            "start": start,
            "end": end,
            "room": room
        }

    def get(self, name):
        """Получение информации о занятии."""
        return self.lessons[name]

    def update(self, name, day, start, end, room):
        """Редактирование занятия."""
        if name not in self.lessons:
            raise KeyError("Занятие не найдено")

        start, end = self.validate(name, day, start, end, room)
        self.check_conflict(day, start, end, room, name)

        self.lessons[name] = {
            "day": day,
            "start": start,
            "end": end,
            "room": room
        }

    def delete(self, name):
        """Удаление занятия."""
        del self.lessons[name]

    def show(self):
        """Вывод расписания."""
        if not self.lessons:
            print("Расписание пусто")
            return

        for name, lesson in self.lessons.items():
            print(
                f"{name}: {lesson['day']}, "
                f"{lesson['start']}-{lesson['end']}, "
                f"аудитория {lesson['room']}"
            )

    def save(self, filename="schedule.json"):
        """Сохранение расписания."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                self.lessons, file,
                ensure_ascii=False, indent=4
            )

    def load(self, filename="schedule.json"):
        """Загрузка расписания."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.lessons = json.load(file)
        except FileNotFoundError:
            self.lessons = {}


def input_lesson():
    """Ввод данных занятия."""
    day = input("День недели: ")
    start = input("Начало (ЧЧ:ММ): ")
    end = input("Конец (ЧЧ:ММ): ")
    room = input("Аудитория: ")
    return day, start, end, room


def main():
    schedule = Schedule()

    try:
        schedule.load()
    except (OSError, ValueError) as error:
        print("Ошибка загрузки:", error)
        return

    while True:
        print("\n1. Добавить занятие")
        print("2. Показать расписание")
        print("3. Редактировать занятие")
        print("4. Удалить занятие")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        try:
            if choice == "1":
                name = input("Название занятия: ")
                schedule.add(name, *input_lesson())
                schedule.save()
                print("Занятие добавлено!")

            elif choice == "2":
                schedule.show()

            elif choice == "3":
                name = input("Название занятия: ")
                schedule.update(name, *input_lesson())
                schedule.save()
                print("Занятие обновлено!")

            elif choice == "4":
                name = input("Название занятия: ")
                schedule.delete(name)
                schedule.save()
                print("Занятие удалено!")

            elif choice == "0":
                print("Программа завершена")
                break

            else:
                print("Неверный пункт меню")

        except (ValueError, KeyError, OSError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
