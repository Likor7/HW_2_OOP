from framework.models import Model


class Toyota(Model):
    file = "toyotas.json"

    def __init__(self, name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color
        self.gear = 0
        self.id = self._create_id()

    def drive(self):
        print("drive")

    def __shift_gear(self, gear):
        self.gear = gear

    @classmethod
    def change_color_by_id(cls, id):
        data = cls._get_all_data()
        data[id-1]["color"] = input("Input color:\t")
        cls._write_data(data)
