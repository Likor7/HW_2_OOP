from models.Toyota import Toyota


def start_framework():
    while True:
        print("Framework for Toyota!\n" +
              "1. Add a new car\n" +
              "2. Get all cars\n" +
              "3. Get a car by id\n" +
              "0. Exit\n")

        try:
            chosen = int(input("Choose item:\t"))
            print("\n")

            if chosen == 1:
                name = input("Input name:\t")
                engine = input("Input engine:\t")
                color = input("Input color:\t")

                new_toyota = Toyota(name, engine, color)
                new_toyota.save()
                print("\n")

            elif chosen == 2:
                Toyota.show_data()
                print("\n")

            elif chosen == 3:
                id = int(input("Input id:\t"))
                if Toyota.size_of_database() < id:
                    print("There is no id like this\n")
                else:
                    Toyota.get_by_id(id)
                    print("\n")

            elif chosen == 4:
                id = int(input("Input id:\t"))
                if Toyota.size_of_database() < id:
                    print("There is no id like this\n")
                else:
                    Toyota.change_color_by_id(id)
                    print("\n")
            else:
                print("Thanks for using my app!")
                break
        except():
            print("Wrong data entered")


if __name__ == "__main__":
    start_framework()
