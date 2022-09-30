from framework.models import Model


class Toyota(Model):
    file = "toyotas.json"

    def __init__(self, name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color
        self.id = self.__create_id()

    def drive(self):
        #Some script to drive
        #while I drive i can shift gear
        pass

    def __shift_gear(self):
        #Some script to shift_gear
        pass

    def change_color_by_id(self, id):
        data = self.__get_all_data()
        data[id]["color"] = input("Input color:\t")
        self.__write_data(data)
