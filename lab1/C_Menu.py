from C_Room import Room
        
class Menu :        
    def __init__(self):  
        self.room = Room()
        self.choice = ""

    def show(self):
        while (self.choice != "q") :
            print(
            """Menu:
            Wprowadz odpowiedni znak aby wybrac opcje:
            1 - pokaz wszystkie miejsca
            2 - pokaz wolne miejsca
            3 - pokaz zarezerwowane miejsca
            4 - zarezerwuj miejsce
            5 - anuluj rezerwacje
            6 - sprawdz dostepnosc miejsca
            q - wyjdz""")
            self.choice = input()
            if self.choice == "1":
                self.room.show_all()
            elif self.choice == "2":
                self.room.show_free()
            elif self.choice == "3":
                self.room.show_taken()
            elif self.choice == "4":
                print("Wprowadz oznaczenie miejsca np. a1")
                seat = input()
                self.room.make_reservation(seat)
            elif self.choice == "5":
                print("Wprowadz oznaczenie miejsca np. a1")
                seat = input()
                self.room.delete_reservation(seat)
            elif self.choice == "6":
                print("Wprowadz oznaczenie miejsca np. a1")
                seat = input()
                self.room.check_seat(seat)
            elif self.choice == "q":
                print("Dziekujemy za wybor naszego kina. Do zobaczenia!")
            else:
                print("Wybrana opcja jest niepoprawna")

M = Menu()
M.show()


# room = Room()
# choice = ""

# def show(choice):
#     while (choice != "q") :
#         print(
#         """Menu:
#         Wprowadz odpowiedni znak aby wybrac opcje:
#         1 - pokaz wszystkie meijsca
#         2 - pokaz wolne miejsca
#         3 - pokaz zarezerwowane miejsca
#         4 - zarezerwuj miejsce
#         5 - anuluj rezerwacje
#         6 - sprawdz dostepnosc miejsca
#         q - wyjdz""")
#         choice = input()
#         if choice == "1":
#             room.show_all()
#         elif choice == "2":
#             room.show_free()
#         elif choice == "3":
#             room.show_taken()
#         elif choice == "4":
#             print("Wprowadz oznaczenie miejsca np. a1")
#             seat = input()
#             room.make_reservation(seat)
#         elif choice == "5":
#             print("Wprowadz oznaczenie miejsca np. a1")
#             seat = input()
#             room.delete_reservation(seat)
#         elif choice == "6":
#             print("Wprowadz oznaczenie miejsca np. a1")
#             seat = input()
#             room.check_seat(seat)
#         elif choice == "q":
#             print("Dziekujemy za wybor naszego kina. Do zobaczenia!")
#         else:
#             print("Wybrana opcja jest niepoprawna")

# show(choice)