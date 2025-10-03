# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any
#
#
# class Builder(ABC):
#     @property
#     @abstractmethod
#     def product(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_a(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_b(self) -> None:
#         pass
#
#     @abstractmethod
#     def produce_part_c(self) -> None:
#         pass
#
#
#
# class ConcreteBuilder1(Builder):
#     def __init__(self) -> None:
#         self.reset()
#
#     def reset(self) -> None:
#         self._product = Product1()
#
#     @property
#     def product(self) -> Product1:
#         product = self._product
#         self.reset()
#         return product
#
#     def produce_part_a(self) -> None:
#         self._product.add("Часть A1")
#
#     def produce_part_b(self) -> None:
#         self._product.add("Часть B1")
#
#     def produce_part_c(self) -> None:
#         self._product.add("Часть C1")
#
#
# class Product1:
#     def __init__(self) -> None:
#         self.parts = []
#
#     def add(self, part: Any) -> None:
#         self.parts.append(part)
#
#     def list_parts(self) -> None:
#         print(f"Части продукта: {', '.join(self.parts)}", end="")
#
#
#
# class Director:
#     def __init__(self) -> None:
#         self._builder = None
#
#     @property
#     def builder(self) -> Builder:
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#         self._builder = builder
#
#     def build_minimal_product(self) -> None:
#         self.builder.produce_part_a()
#
#     def build_full_product(self) -> None:
#         self.builder.produce_part_a()
#         self.builder.produce_part_b()
#         self.builder.produce_part_c()
#
#
# if __name__ == "__main__":
#     director = Director()
#     builder = ConcreteBuilder1()
#     director.builder = builder
#
#     print("Минимальный продукт:")
#     director.build_minimal_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     print("Полный продукт:")
#     director.build_full_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     print("Кастомный продукт (без директора):")
#     builder.produce_part_a()
#     builder.produce_part_b()
#     builder.product.list_parts()







"""
lessons_oop_and_more.py

Simple script that defines 8 lessons (in Russian) with descriptions and
exports them to Markdown. Ready to edit.
"""

from dataclasses import dataclass, field
from typing import List
import datetime


@dataclass
class Lesson:
    number: int
    title: str
    objectives: List[str]
    topics: List[str]
    exercises: List[str]
    resources: List[str] = field(default_factory=list)
    duration_minutes: int = 90

    def to_markdown(self) -> str:
        md = []
        md.append(f"# Урок {self.number}. {self.title}\n")
        md.append(f"**Длительность:** {self.duration_minutes} минут\n")
        md.append("## Цели урока\n")
        for obj in self.objectives:
            md.append(f"- {obj}")
        md.append("\n## Ключевые темы\n")
        for t in self.topics:
            md.append(f"- {t}")
        md.append("\n## Практические задания / упражнения\n")
        for ex in self.exercises:
            md.append(f"- {ex}")
        if self.resources:
            md.append("\n## Ресурсы и ссылки\n")
            for r in self.resources:
                md.append(f"- {r}")
        md.append("\n---\n")
        return "\n".join(md)


def build_lessons() -> List[Lesson]:
    lessons: List[Lesson] = []

    lessons.append(
        Lesson(
            number=1,
            title="ООП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование",
            objectives=[
                "Понять основные концепции ООП: класс, объект, атрибут, метод.",
                "Научиться объявлять классы и создавать экземпляры.",
                "Понять и применить наследование для повторного использования кода.",
            ],
            topics=[
                "Конструктор __init__ и атрибуты экземпляра",
                "Методы экземпляра и методы класса",
                "Наследование: базовый и дочерний классы, super()",
                "Примеры: классы Animal -> Dog/ Cat, базовый Product -> Chair/ Sofa",
            ],
            exercises=[
                "Создать класс Person с атрибутами name, age и методом greet().",
                "Реализовать классы Vehicle и Car (Car наследует Vehicle) и показать переиспользование.",
                "Задание: модель простого каталога товаров — базовый Product и наследуемые категории."
            ],
            resources=["Официальная документация Python: раздел про классы", "Книга: 'Python OOP' — глава 1"],
            duration_minutes=90,
        )
    )

    lessons.append(
        Lesson(
            number=2,
            title="ООП 2: Другие принципы ООП - Инкапсуляция, Полиморфизм",
            objectives=[
                "Понять инкапсуляцию и уровни доступа (public/protected/private в Python-подходе).",
                "Изучить полиморфизм и интерфейсы в динамическом Python.",
            ],
            topics=[
                "Скрытие данных: соглашение _protected и __private (name mangling)",
                "Геттеры/сеттеры (property)",
                "Полиморфизм: одинаковый интерфейс — разные реализации",
                "Duck typing: 'если выглядит как утка...'",
            ],
            exercises=[
                "Реализовать класс BankAccount c приватным балансом и property для безопасного доступа.",
                "Создать две реализации интерфейса Logger (ConsoleLogger, FileLogger) и продемонстрировать полиморфизм."
            ],
            resources=["PEP: property(), обсуждение инкапсуляции в Python"],
            duration_minutes=90,
        )
    )

    lessons.append(
        Lesson(
            number=3,
            title="Магические, статичные, классовые методы в классах, множественное наследование",
            objectives=[
                "Изучить магические (dunder) методы для управления поведением объектов.",
                "Понять разницу между @staticmethod и @classmethod.",
                "Разобраться с правилами множественного наследования (MRO).",
            ],
            topics=[
                "Магические методы: __str__, __repr__, __eq__, __len__, __iter__, __enter__/__exit__",
                "@staticmethod vs @classmethod: когда и зачем",
                "Множественное наследование и Method Resolution Order (MRO)",
                "Примеры: фабричные методы, контекстные менеджеры"
            ],
            exercises=[
                "Добавить __repr__ и __eq__ в класс Product для удобства отладки.",
                "Реализовать фабричный метод (classmethod) для создания объекта из словаря.",
                "Демонстрация MRO: создать классы A, B, C с перекрывающимися методами и вывести C.__mro__."
            ],
            resources=["Документация: data model (magic methods)"],
            duration_minutes=90,
        )
    )

    lessons.append(
        Lesson(
            number=4,
            title="Закрепление пройденного материала - Использование ООП в проекте",
            objectives=[
                "Применить ранее изученные концепции ООП в небольшом проекте.",
                "Закрепить архитектурные практики: разделение ответственности между классами.",
            ],
            topics=[
                "Проект: мини-магазин (каталог, корзина, заказ) с использованием классов",
                "SOLID в контексте Python (кратко)",
                "Организация модулей и тестирование",
            ],
            exercises=[
                "Разработать простую структуру проекта: models.py, services.py, app.py с OOP-подходом.",
                "Написать несколько unit-тестов для ключевых классов (pytest)."
            ],
            resources=["Шаблоны проектной структуры на GitHub"],
            duration_minutes=120,
        )
    )

    lessons.append(
        Lesson(
            number=5,
            title="Виртуальная среда, встроенные модули Python, определение собственных модулей, внешние модули и их установка, Основы GIT",
            objectives=[
                "Научиться работать с виртуальными окружениями (venv, pipenv, virtualenv).",
                "Понять структуру модулей и пакетов в Python и как импортировать их.",
                "Установить внешние зависимости и использовать pip, requirements.txt.",
                "Знать базовые команды Git и рабочий цикл (commit, push, branch)."
            ],
            topics=[
                "venv: создание, активация, установка пакетов",
                "Структура пакета: __init__.py, относительные импорты",
                "pip, pip freeze > requirements.txt, pip install -r requirements.txt",
                "Git: init, add, commit, push, pull, branch, merge, .gitignore"
            ],
            exercises=[
                "Создать venv, установить pytest и сохранить requirements.txt.",
                "Инициализировать Git-репозиторий, сделать первый коммит с простым README."
            ],
            resources=["Git cheat sheet", "Python packaging tutorial"],
            duration_minutes=90,
        )
    )

    lessons.append(
        Lesson(
            number=6,
            title="Структуры данных и алгоритмы. Big O нотация, рекурсия",
            objectives=[
                "Изучить стандартные структуры данных: списки, множества, словари, очереди, стеки, деревья.",
                "Понять Big O нотацию и оценивать сложность алгоритмов.",
                "Разобраться с рекурсией и её применением.",
            ],
            topics=[
                "Time/Space complexity, примеры O(1), O(n), O(n^2), O(log n)",
                "Стек/очередь: реализация и применение",
                "Рекурсивные алгоритмы: факториал, обход дерева, quicksort/merge sort концепции",
                "Хэш-таблицы (dict) и их амортизированная сложность"
            ],
            exercises=[
                "Оценить сложность простых функций и алгоритмов.",
                "Реализовать рекурсивный обход дерева и итеративную версию (если возможно).",
                "Реализовать простую функцию поиска бинарного дерева (binary search)."
            ],
            resources=["CLRS (главы по сложностям и структурам данных)"],
            duration_minutes=120,
        )
    )

    lessons.append(
        Lesson(
            number=7,
            title="Базы данных и СУБД. Работа с БД в Python. Основы SQL, создание таблиц и типы данных, CRUD операции",
            objectives=[
                "Понять, что такое СУБД и чем отличаются реляционные/нереляционные БД.",
                "Научиться писать базовые SQL-запросы: CREATE, SELECT, INSERT, UPDATE, DELETE.",
                "Подключаться к БД из Python (sqlite3/psycopg2/SQLAlchemy) и выполнять CRUD операции.",
            ],
            topics=[
                "Типы данных в SQL (INTEGER, TEXT/VARCHAR, DATE, BOOLEAN, FLOAT, SERIAL)",
                "CREATE TABLE, PRIMARY KEY, FOREIGN KEY, индексы",
                "CRUD: примеры SQL и использование в Python",
                "Коротко: ORM (SQLAlchemy) vs чистые SQL-запросы"
            ],
            exercises=[
                "Создать локальную sqlite DB, таблицу users и products, выполнить CRUD операции из Python.",
                "Написать простой скрипт миграции (создание таблиц) и заполнения тестовыми данными."
            ],
            resources=["Документация SQLite, SQL cheat sheet"],
            duration_minutes=120,
        )
    )

    lessons.append(
        Lesson(
            number=8,
            title="Реляционные базы данных и типы соотношения таблиц. Агрегационные функции и группировка данных. Вложенные запросы. Views",
            objectives=[
                "Понять типы связей: 1:1, 1:N, M:N и как их реализовать в схеме БД.",
                "Изучить агрегатные функции (COUNT, SUM, AVG, MIN, MAX) и GROUP BY.",
                "Понять вложенные запросы (subqueries) и виртуальные таблицы (views).",
            ],
            topics=[
                "Проектирование схемы с отношениями (foreign keys, junction tables)",
                "Агрегация и группировка: примеры и кейсы",
                "Subqueries: коррелированные и некоррелированные",
                "Views: создание и использование, ограничения и преимущества"
            ],
            exercises=[
                "Спроектировать схему для магазина: users, products, orders, order_items (M:N через order_items).",
                "Написать запрос, показывающий total sales по товарам (используя GROUP BY и SUM).",
                "Создать view, который объединяет таблицы orders и users для отчетов."
            ],
            resources=["SQL advanced queries guide"],
            duration_minutes=120,
        )
    )

    return lessons


def print_summary(lessons: List[Lesson]):
    print("Краткое содержание курса (generated on {}):\n".format(datetime.date.today()))
    for lesson in lessons:
        print(f"Урок {lesson.number}: {lesson.title}")
        print("  - Цели:", "; ".join(lesson.objectives[:2]) + ("..." if len(lesson.objectives) > 2 else ""))
        print("  - Практика:", f"{len(lesson.exercises)} задания(й)")
        print()


def export_to_markdown(lessons: List[Lesson], filename: str = "lessons.md"):
    header = f"## План курса — OOP и сопутствующие темы\n_Сгенерировано: {datetime.date.today()}_\n\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header)
        for lesson in lessons:
            f.write(lesson.to_markdown())
    print(f"Экспорт завершён: {filename}")


if __name__ == "__main__":
    lessons = build_lessons()
    print_summary(lessons)
    export_to_markdown(lessons)
