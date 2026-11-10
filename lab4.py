class Hotel:

    def __init__(self, name="Невідомо", rooms_count=0, visitors_per_year=0,
                 city="Невідомо", category="немає", stars=0):

        self.__name = name
        self.__rooms_count = rooms_count
        self.__visitors_per_year = visitors_per_year

        self._city = city

        self.stars = stars
        self.category = category

    def get_name(self):
        return self.__name

    def get_rooms_count(self):
        return self.__rooms_count

    def get_visitors_per_year(self):
        return self.__visitors_per_year

    def set_name(self, name):
        self.__name = name

    def set_rooms_count(self, rooms_count):
        if rooms_count < 0:
            print("Кількість номерів не може бути від'ємною")
        else:
            self.__rooms_count = rooms_count

    def set_visitors_per_year(self, visitors_per_year):
        if visitors_per_year < 0:
            print("Кількість відвідувачів не може бути від'ємною")
        else:
            self.__visitors_per_year = visitors_per_year

    def __str__(self):
        return (f"Готель «{self.__name}»: номерів - {self.__rooms_count}, "
                f"відвідувачів на рік - {self.__visitors_per_year}, "
                f"місто - {self._city}, зірок - {self.stars}, "
                f"категорія - {self.category}")

    def __repr__(self):
        return (f"Hotel(name={self.__name!r}, rooms_count={self.__rooms_count!r}, "
                f"visitors_per_year={self.__visitors_per_year!r}, city={self._city!r}, "
                f"category={self.category!r}, stars={self.stars!r})")

    
    def __add__(self, other):
        return self.__rooms_count + other.__rooms_count

    def __sub__(self, other):
        return self.__visitors_per_year - other.__visitors_per_year

    def __mul__(self, number):
        return self.__rooms_count * number

    def __truediv__(self, other):
        if other.__rooms_count == 0:
            print("Ділити на нуль не можна")
            return None
        return self.__rooms_count / other.__rooms_count

    def __floordiv__(self, other):
        if other.__rooms_count == 0:
            print("Ділити на нуль не можна")
            return None
        return self.__rooms_count // other.__rooms_count

    
    def __gt__(self, other):
        return self.__rooms_count > other.__rooms_count

    def __lt__(self, other):
        return self.__rooms_count < other.__rooms_count

    def __del__(self):
        print(f"Об'єкт «{self.__name}» знищено")


def main():
    hotel1 = Hotel()
    hotel2 = Hotel("Grand Hotel", 120, 35000, "Київ", "люкс", 5)
    hotel3 = Hotel("Карпати", 60, 12000, "Яремче", "стандарт", 3)

    hotel1.set_name("Львів")
    hotel1.set_rooms_count(85)
    hotel1.set_visitors_per_year(20000)
    hotel1.stars = 4
    hotel1.category = "бізнес"

    hotels = [hotel1, hotel2, hotel3]

    for i, h in enumerate(hotels, start=1):
        print(f"--- Готель {i} ---")
        print("Назва:", h.get_name())
        print("Кількість номерів:", h.get_rooms_count())
        print("Відвідувачів на рік:", h.get_visitors_per_year())
        print("Місто (protected):", h._city)
        print("Зірок (public):", h.stars)
        print("Категорія (public):", h.category)
        print("__str__ :", str(h))
        print("__repr__:", repr(h))
        print()

    
    def get_stars(h):
        return h.stars

    by_stars = sorted(hotels, key=get_stars, reverse=True)

    print("Сортування за зірками")
    for h in by_stars:
        print(h.get_name(), "-", h.stars, "зірок")
    print()

    
    print("Порівняння")
    if hotel1.get_rooms_count() > hotel3.get_rooms_count():
        print(hotel1.get_name(), "має більше номерів, ніж", hotel3.get_name())
    else:
        print(hotel3.get_name(), "має не менше номерів, ніж", hotel1.get_name())

    if hotel2.stars > hotel3.stars:
        print(hotel2.get_name(), "має більше зірок, ніж", hotel3.get_name())
    else:
        print(hotel2.get_name(), "має не більше зірок, ніж", hotel3.get_name())
    print()

    
    print("Додавання")
    total_rooms = sum(h.get_rooms_count() for h in hotels)
    total_visitors = sum(h.get_visitors_per_year() for h in hotels)
    total_stars = sum(h.stars for h in hotels)
    print("Усього номерів:", total_rooms)
    print("Усього відвідувачів на рік:", total_visitors)
    print("Сума зірок:", total_stars)
    print()

    
    print("Віднімання")
    diff_visitors = hotel2 - hotel3
    diff_rooms = hotel2.get_rooms_count() - hotel3.get_rooms_count()
    print("Різниця у відвідувачах:", diff_visitors)
    print("Різниця у номерах:", diff_rooms)
    print()

    print(hotel2 - hotel3)            
    print(hotel2.__sub__(hotel3))
    


    
    print("Множення")
    price = 1500
    income = hotel2.get_rooms_count() * price
    print("Дохід за ніч (Grand Hotel, усі номери зайняті):", income, "грн")
    print()

    
    print("Ділення")
    avg_visitors = total_visitors / len(hotels)
    print("Середня кількість відвідувачів на готель:", round(avg_visitors, 2))
    print()

    
    print("Оператори між об'єктами")
    print("hotel2 + hotel3 =", hotel2 + hotel3)    
    print("hotel2 - hotel3 =", hotel2 - hotel3)      
    print("hotel2 * 1500   =", hotel2 * 1500)        
    print("hotel2 / hotel3 =", hotel2 / hotel3)      
    print("hotel2 // hotel3 =", hotel2 // hotel3)   
    print()


    print("Порівняння об'єктів напряму (за номерами)")
    if hotel1 > hotel3:
        print(hotel1.get_name(), "більший за", hotel3.get_name())
    else:
        print(hotel1.get_name(), "не більший за", hotel3.get_name())

    if hotel3 < hotel2:
        print(hotel3.get_name(), "менший за", hotel2.get_name())
    else:
        print(hotel3.get_name(), "не менший за", hotel2.get_name())
    print()


    del hotel3
    print("Vfq;t rsytwm")




if __name__ == "__main__":
    main()