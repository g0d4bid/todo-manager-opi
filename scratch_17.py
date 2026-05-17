class RoomItem:
    """Базовый класс для всех предметов в квартире"""

    def __init__(self, name, room, material, color):
        self.__name = name  # инкапсуляция
        self.__room = room
        self.__material = material
        self.__color = color
        self.__condition = "новый"

    # Геттеры (инкапсуляция)
    def get_name(self):
        return self.__name

    def get_room(self):
        return self.__room

    def get_material(self):
        return self.__material

    def get_color(self):
        return self.__color

    def get_condition(self):
        return self.__condition

    # Сеттеры (инкапсуляция)
    def set_condition(self, condition):
        if condition in ["новый", "хороший", "средний", "плохой", "сломан"]:
            self.__condition = condition
        else:
            print(f"Некорректное состояние: {condition}")

    def set_color(self, color):
        self.__color = color

    # Полиморфизм: метод будет переопределен в дочерних классах
    def get_info(self):
        return f"{self.__name} ({self.__room}) - Материал: {self.__material}, Цвет: {self.__color}, Состояние: {self.__condition}"


class Furniture(RoomItem):
    """Подкласс: Мебель"""

    def __init__(self, name, room, material, color, furniture_type, has_storage=False):
        super().__init__(name, room, material, color)
        self.__furniture_type = furniture_type
        self.__has_storage = has_storage
        self.__drawers = 0

    # Дополнительные геттеры для мебели
    def get_furniture_type(self):
        return self.__furniture_type

    def has_storage(self):
        return self.__has_storage

    def get_drawers(self):
        return self.__drawers

    # Дополнительные сеттеры
    def set_drawers(self, drawers):
        self.__drawers = drawers

    # Полиморфизм: переопределение метода
    def get_info(self):
        base_info = super().get_info()
        storage = "есть" if self.__has_storage else "нет"
        return f"{base_info}, Тип: {self.__furniture_type}, Хранение: {storage}, Ящиков: {self.__drawers}"


class Appliance(RoomItem):
    """Подкласс: Бытовая техника"""

    def __init__(self, name, room, material, color, power_w, is_smart=False):
        super().__init__(name, room, material, color)
        self.__power_w = power_w
        self.__is_smart = is_smart
        self.__is_turned_on = False

    def get_power(self):
        return self.__power_w

    def is_smart(self):
        return self.__is_smart

    def is_turned_on(self):
        return self.__is_turned_on

    # Специфичные методы для техники
    def turn_on(self):
        self.__is_turned_on = True
        return f"{self.get_name()} включен(а)"

    def turn_off(self):
        self.__is_turned_on = False
        return f"{self.get_name()} выключен(а)"

    # Полиморфизм: переопределение метода
    def get_info(self):
        base_info = super().get_info()
        smart = "умная" if self.__is_smart else "обычная"
        status = "вкл" if self.__is_turned_on else "выкл"
        return f"{base_info}, Мощность: {self.__power_w}Вт, Тип: {smart}, Статус: {status}"


class Decor(RoomItem):
    """Подкласс: Декор и украшения"""

    def __init__(self, name, room, material, color, decor_style, is_fragile=True):
        super().__init__(name, room, material, color)
        self.__decor_style = decor_style
        self.__is_fragile = is_fragile
        self.__is_wall_mounted = False

    def get_decor_style(self):
        return self.__decor_style

    def is_fragile(self):
        return self.__is_fragile

    def is_wall_mounted(self):
        return self.__is_wall_mounted

    def mount_on_wall(self):
        self.__is_wall_mounted = True
        return f"{self.get_name()} размещен(а) на стене"

    # Полиморфизм: переопределение метода
    def get_info(self):
        base_info = super().get_info()
        fragile = "хрупкий" if self.__is_fragile else "прочный"
        mounted = "на стене" if self.__is_wall_mounted else "не закреплен"
        return f"{base_info}, Стиль: {self.__decor_style}, Прочность: {fragile}, Размещение: {mounted}"


class Apartment:
    """Класс для управления коллекцией предметов в квартире"""

    def __init__(self, address):
        self.__address = address
        self.__items = []  # список всех предметов

    def add_item(self, item):
        """Добавление предмета в квартиру"""
        self.__items.append(item)
        print(f"Добавлен предмет: {item.get_name()}")

    def remove_item(self, name):
        for i, item in enumerate(self.__items):
            if item.get_name().lower() == name.lower():
                removed = self.__items.pop(i)
                print(f"Удален предмет: {removed.get_name()}")
                return True
        print(f"Предмет с названием '{name}' не найден")
        return False

    def find_by_name(self, name):
        result = []
        for item in self.__items:
            if name.lower() in item.get_name().lower():
                result.append(item)
        return result

    def find_by_room(self, room):
        result = []
        for item in self.__items:
            if item.get_room().lower() == room.lower():
                result.append(item)
        return result

    def find_by_type(self, item_type):
        result = []
        for item in self.__items:
            if item.__class__.__name__ == item_type:
                result.append(item)
        return result

    def show_all_items(self):
        if not self.__items:
            print("В квартире пока нет предметов")
            return

        print(f"\n=== Квартира по адресу: {self.__address} ===")
        print(f"Всего предметов: {len(self.__items)}")
        print("-" * 50)

        rooms = {}
        for item in self.__items:
            room = item.get_room()
            if room not in rooms:
                rooms[room] = []
            rooms[room].append(item)

        for room, items in rooms.items():
            print(f"\n--- {room.upper()} ({len(items)} предметов) ---")
            for item in items:
                print(f"  • {item.get_info()}")

    def get_item_count(self):
        return len(self.__items)

    def get_items_by_condition(self, condition):
        return [item for item in self.__items if item.get_condition() == condition]

    def change_item_color(self, name, new_color):
        items = self.find_by_name(name)
        if items:
            for item in items:
                item.set_color(new_color)
                print(f"Цвет предмета '{item.get_name()}' изменен на {new_color}")
            return True
        return False