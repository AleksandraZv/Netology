class FarmAnimals:
    amount_of_feeding_per_day = 3  # раз в день
    walk_per_day = 3  # раз в день
    bathing = 2  # раз в день
    sleep_hour = 8  # часов в день

    def feed(self):
        pass

    def walk(self):
        pass

    def bath(self):
        pass

    def sleep(self):
        pass


class Сow(FarmAnimals):
    milk = 2  # раза в день

    def milk(self):
        print('Корова подоена')


class Goat(FarmAnimals):
    soda_treatment = 1  # раз в неделю

    def soda_treatment(self):
        print('Шкура козла обработана содой')


class Sheep(FarmAnimals):
    stall_processing = 1  # раз в месяц

    def stall_processing(self):
        print('Стойла овец очищены')


class Pigs (FarmAnimals):
    mud_bath = 2  # раза в день

    def mud_bath(self):
        print('Все свиньи приняли грязевую ванну')


class DuckBird (FarmAnimals):
    pick_up_eggs = 1  # раз в день

    def pick_up_eggs(self):
        print('У уток собраны яйца')


class Chicken(FarmAnimals):
    feed_worms = 1  # раз в день

    def feed_worms(self):
        print('Все курицы накормлены червяками')


class GusBird(FarmAnimals):
    paint_feathers = 1  # раз в месяц

    def paint_feathers(self):
        print('Всем гусям были раскрашены перья')

animal = FarmAnimals()
farm_cow = Сow

farm_cow.milk(2)