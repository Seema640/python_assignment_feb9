class student:
    def __init__(self,fstr,lstr):
            self.fstr=fstr
            self.lstr=lstr

    def get_string(self):
        self.fstr=fstr
    def get_string2(self):
        self.lstr=lstr
    def update_firstname(self):
        print("Dear {}{},I would like to ............".format(self.fstr,self.lstr))

fstr=input("Enter your firstname:")
lstr=input("Enter your lastname:")
s=student("fstr","lstr")
s.get_string()
s.get_string2()
s.update_firstname()





