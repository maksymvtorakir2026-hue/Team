class Musician:

    def __init__(self, name="Невідомий виконавець", fee=0, age=0):
        if fee < 0:
            raise ValueError("Гонорар не може бути від'ємним")
        if age < 0:
            raise ValueError("Вік не може бути від'ємним")

        self.__name = name
        self.__fee = fee
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_fee(self):
        return self.__fee

    def set_fee(self, fee):
        if fee < 0:
            raise ValueError("Гонорар не може бути від'ємним")
        self.__fee = fee

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Вік не може бути від'ємним")
        self.__age = age

    def __str__(self):
        return f"{self.__name} (вік: {self.__age}, гонорар: {self.__fee:,} грн)"

    def __repr__(self):
        return (
            f"Musician(name={self.__name!r}, "
            f"fee={self.__fee!r}, age={self.__age!r})"
        )

    def __del__(self):
        print(f"Об'єкт «{self.__name}» знищено")


class MusicFestival:

    def __init__(self, budget=0, musicians=None):
        if budget < 0:
            raise ValueError("Бюджет не може бути від'ємним")

        self.__budget = budget
        self.__musicians = []

        for musician in musicians or []:
            self.add_musician(musician)

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        if budget < 0:
            raise ValueError("Бюджет не може бути від'ємним")
        if budget < self.get_total_fees():
            raise ValueError("Гонорар перевищує бюджет")
        self.__budget = budget


    def get_musicians(self):
        return self.__musicians.copy()

    def get_total_fees(self):
        return sum(musician.get_fee() for musician in self.__musicians)

    def get_remaining_budget(self):
        return self.__budget - self.get_total_fees()

    def add_musician(self, musician):
        if not isinstance(musician, Musician):
            raise TypeError("До фестивалю можна додавати лише об'єкти Musician")

        if musician.get_fee() > self.get_remaining_budget():
            print(
                f"Не додано {musician.get_name()}: "
                "не вистачає бюджету."
            )
            return False

        self.__musicians.append(musician)
        print(f"Додано виконавця: {musician.get_name()}")
        return True

    def remove_musician(self, name):
        for musician in self.__musicians:
            if musician.get_name() == name:
                self.__musicians.remove(musician)
                print(f"Видалено виконавця: {name}")
                return True

        print(f"Виконавця {name} у списку немає.")
        return False

    def __str__(self):
        names = ", ".join(
            musician.get_name() for musician in self.__musicians
        ) or "поки немає"

        return (
            f"Музичний фестиваль: бюджет {self.__budget:,} грн; "
            f"витрачено {self.get_total_fees():,} грн; "
            f"залишок {self.get_remaining_budget():,} грн; "
            f"виконавці: {names}"
        )

    def __repr__(self):
        return (
            f"MusicFestival(budget={self.__budget!r}, "
            f"musicians={self.__musicians!r})"
        )

    def __del__(self):
        pass


def main():
    musicians = [
        Musician("Океан Ельзи", 500000, 30),
        Musician("The Hardkiss", 300000, 15),
        Musician("Без Обмежень", 250000, 20),
        Musician("Молодий гурт", 100000, 5),
    ]

    festival = MusicFestival(900000, musicians)

    print("\nСтан фестивалю після створення:")
    print(festival)

    print("\nДетальна інформація про запрошених виконавців:")
    for musician in festival.get_musicians():
        print(musician)

    festival.add_musician(
        Musician("Новий виконавець", 50000, 22)
    )
    print("\nПісля спроби додавання:")
    print(festival)

    festival.remove_musician("The Hardkiss")
    print("\nПісля видалення The Hardkiss:")
    print(festival)

    festival.add_musician(
        Musician("Запрошена зірка", 300000, 28)
    )
    print("\nФінальний стан фестивалю:")
    print(festival)


if __name__ == "__main__":
    main()