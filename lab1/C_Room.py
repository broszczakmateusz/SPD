import re
from C_Row import Row
from C_Reservation import Reservation

class Room:
    def __init__(self):   
        self.rows = []
        self._which_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self._which_column = []
        self.reservations = {}
   
        for row in range(8):
            tmp = Row()
            self.rows.append(tmp)
        for x in range(16):
            seatname = str(x+1).zfill(2)
            self._which_column.append(seatname)

    def _index_r_c(self, seatname): #dodac ochrone przed wprowadzeiem zlych danych
        seatname.lower().strip()
        row  = seatname[0]
        tmp = int(re.search(r'\d+', seatname).group())
        column = str(tmp).zfill(2)

        r = self._which_row.index(row)
        c = self._which_column.index(column)
        return r, c

    def _is_free(self, row, column):
        row_to_check = self.rows[row] 
        return row_to_check.is_free(column) 

    def _is_taken(self, row, column):
        row_to_check = self.rows[row] 
        return row_to_check.is_taken(column) 

    def make_reservation(self, seat):
        row, column = self._index_r_c(seat)
        if self._is_free(row, column) == True:
            self.rows[row].take_a_seat(column) 

            print("Wprowadz imie")
            first_name = input()
            print("Wprowadz nazwisko")
            last_name = input()

            seatname = f"{self._which_row[row].upper}{str(self._which_column[column]).zfill(2)}"
            self.reservations[seatname] = (Reservation(first_name, last_name, seatname)) 
            print("Udalo sie zarezerwowac miejsce")
        elif self._is_taken(row, column) == True:
            print("To miejsce jest zajete")
        else:
            print("Nie ma takiego miejsca")

    def delete_reservation(self, seat):
        row, column = self._index_r_c(seat)
        seatname = f"{self._which_row[row].upper}{str(self._which_column[column]).zfill(2)}"

        # if seatname in self.all_resevations:
        res = self.reservations[seatname]

        if self._is_taken(row, column) == True:
            print("Wprowadz imie")
            first_name = input()
            print("Wprowadz nazwisko")
            last_name = input()
            if first_name == res.first_name and last_name == res.last_name:
                    self.rows[row].realase_a_seat(column) 
                    self.reservations.pop(seatname)
            else:
                print("Anulowac rezerwacje mozna tylko osobiscie")
    # else:
            # print("Brak rezerwacji na to miejsce")

    def show_all(self):
        s = ""
        for r in self._which_row:
            i = self._which_row.index(r)
            row = str(self._which_row[i])
            s = f"{row}: "
            s+= self.rows[i].get_row_str()
            print(s)

    def show_free(self):
        s = ""
        for r in self._which_row:
            i = self._which_row.index(r)
            row = str(self._which_row[i])
            s = f"{row}: "
            s+= self.rows[i].get_free_str()
            print(s)

    def show_taken(self):
        s = ""
        for r in self._which_row:
            i = self._which_row.index(r)
            row = str(self._which_row[i])
            s = f"{row}: "
            s+= self.rows[i].get_taken_str()
            print(s)     

    def check_seat(self, seat):
        row, column = self._index_r_c(seat)
        if self._is_free(row, column):
            print("Wybrane miejsce jest wolne")
        elif self._is_taken(row, column):
            print("Wybrane miejsce jest zajeste")
        else:
            "Wystapil blad"


