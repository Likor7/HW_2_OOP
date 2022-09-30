import json
from abc import ABC


class Model(ABC):
    @classmethod
    def __get_all_data(cls):
        file = open("database/" + cls.file, "r")
        data = json.load(file)
        file.close()
        return data

    @classmethod
    def size_of_database(cls):
        return len(cls.__get_all_data())

    @classmethod
    def show_data(cls):
        print("Data of this file:\n")
        for i in cls.__get_all_data():
            print(i)

    @classmethod
    def get_by_id(cls, id):
        print("Result:\n:", [result for result in cls.__get_all_data() if result['id'] == id][0])

    def __create_id(self):
        return len(self.__get_all_data()) + 1

    def __write_data(self, data):
        file = open("database/" + self.file, "w")

        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()

    def save(self):
        data = self.__get_all_data()

        data.append(self.__dict__)

        self.__write_data(data)