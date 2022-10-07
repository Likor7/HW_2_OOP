import json
from abc import ABC


class Model(ABC):
    @classmethod
    def _get_all_data(cls):
        file = open("database/" + cls.file, "r")
        data = json.load(file)
        file.close()
        return data

    @classmethod
    def size_of_database(cls):
        return len(cls._get_all_data())

    @classmethod
    def show_data(cls):
        print("Data of this file:\n")
        for i in cls._get_all_data():
            print(i)

    @classmethod
    def get_by_id(cls, id):
        print("Result:", [cls._get_all_data()[id-1]][0])

    def _create_id(self):
        return self.size_of_database() + 1

    @classmethod
    def _write_data(cls, data):
        file = open("database/" + cls.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        file.close()

    def save(self):
        data = self._get_all_data()
        data.append(self.__dict__)
        self._write_data(data)
