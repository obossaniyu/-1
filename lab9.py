import json
import xml.etree.ElementTree as ET
from lab7 import Employee


def save_json(employee):
    data = {
        "name": employee.name,
        "position": employee.position,
        "salary": employee.salary,
        "experience": employee.experience
    }

    with open("employee.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json():
    with open("employee.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return Employee(
        data["name"],
        data["position"],
        float(data["salary"]),
        int(data["experience"])
    )


def save_xml(employee):
    root = ET.Element("Employee")

    ET.SubElement(root, "name").text = employee.name
    ET.SubElement(root, "position").text = employee.position
    ET.SubElement(root, "salary").text = str(employee.salary)
    ET.SubElement(root, "experience").text = str(employee.experience)

    with open("employee.xml", "wb") as file:
        ET.ElementTree(root).write(
            file,
            encoding="utf-8",
            xml_declaration=True
        )


def load_xml():
    with open("employee.xml", "rb") as file:
        root = ET.parse(file).getroot()

    return Employee(
        root.findtext("name"),
        root.findtext("position"),
        float(root.findtext("salary")),
        int(root.findtext("experience"))
    )


def main():
    try:
        name = input("Введите ФИО: ")
        position = input("Введите должность: ")
        salary = float(input("Введите оклад: "))
        experience = int(input("Введите стаж: "))

        if salary < 0 or experience < 0:
            raise ValueError("Отрицательные значения недопустимы")

        employee = Employee(name, position, salary, experience)

        save_json(employee)
        save_xml(employee)

        print("\nДанные сохранены в JSON и XML")

        print("\nЧтение из JSON:")
        load_json().info()

        print("\nЧтение из XML:")
        load_xml().info()

    except FileNotFoundError:
        print("Ошибка! Файл не найден")

    except PermissionError:
        print("Ошибка! Нет доступа к файлу")

    except json.JSONDecodeError:
        print("Ошибка формата JSON")

    except ET.ParseError:
        print("Ошибка формата XML")

    except (ValueError, TypeError, KeyError):
        print("Ошибка! Некорректные данные")

    except OSError as error:
        print("Ошибка работы с файлом:", error)


if __name__ == "__main__":
    main()