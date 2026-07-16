class Smartphone:
    def __init__(self):
        self.__battery = 100 

    def check_battery(self):
        print(f"バッテリーの残りは {self.__battery}% です")

my_phone = Smartphone()

# my_phone.__battery = 10000 

my_phone.check_battery()
