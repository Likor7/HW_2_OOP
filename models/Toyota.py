import json


class Toyota:
    file = "toyotas.json"

    def __init__(self, name, engine, color, id):
        self.__name = name
        self.__engine = engine
        self.__color = color
        self.__id = id

    # @property
    # def name(self):
    #     return self.__name
    #
    # @property
    # def engine(self):
    #     return self.__engine
    #
    # @property
    # def color(self):
    #     return self.__color
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @engine.setter
    # def engine(self, value):
    #     self.__engine = value
    #
    # @color.setter
    # def color(self, value):
    #     self.__color = value

    def save(self):
        file = open("database/" + self.file, "r")
        data = json.load(file)
        file.close()

        data.append(self.__dict__)
        file = open("database/" + self.file, "w")
        
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()

    @classmethod
    def get_all_data(cls):
        file = open("database/" + cls.file, "r")
        data = json.load(file)

        print(data)
