class Row:
    def __init__(self): 
        self.seats = []
        self.free = []
        self.taken = []
        for x in range(16):
            seatname = str(x+1).zfill(2)
            self.seats.append(seatname)

        self.free = self.seats.copy()

    def get_row_str(self):
        s = ""
        for seat in self.seats:
            s += f"{seat} "
        return s

    def get_free_str(self):
        s = ""
        for f in self.free:
            s += f"{f} "
        return s

    def get_taken_str(self):
        s = ""
        for t in self.taken:
            s += f"{t} "
        return s      

    def take_a_seat(self, number):
        if self.is_free(number):
            x = str(number+1).zfill(2)
            self.taken.append(x)
            i = self.free.index(x)
            self.free.pop(i)
            self.free.sort()
            self.taken.sort()

    def realase_a_seat(self, number):
        if self.is_taken(number):
            x = str(number+1).zfill(2)
            self.free.append(x)
            i = self.taken.index(x)
            self.taken.pop(i)
            self.free.sort()
            self.taken.sort()


    def is_free(self, number):
        x = str(number+1).zfill(2)
        if x in self.free:
            return True
        else:
            return False

    def is_taken(self, number):
        return not self.is_free(number)