from models.Toyota import Toyota


def start_framework():
    while True:
        print("Framework for Toyota!\n" +
              "1. Add a new car\n" +
              "2. Get all cars\n" +
              "3. Get a car by id\n" +
              "0. Exit\n")

        chosen = int(input("Chose item:\t"))
        if chosen == 1:
            name = input("Input name:\t")
            engine = input("Input engine:\t")
            color = input("Input color:\t")
            id = input("Input id:\t")

            new_toyota = Toyota(name, engine, color, id)
            new_toyota.save()

        elif chosen == 2:
            Toyota.get_all_data()

        elif chosen == 3:
            pass
        elif chosen == 0:
            print("Thanks for using my app!")
            break


if __name__ == "__main__":
    start_framework()
