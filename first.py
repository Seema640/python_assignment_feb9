class string:
    def __init__(self,str):
        self.str=str
    def get_string(self):
        self.str=str
    def print_string(self):
        self.str=self.str.upper()


str=input("Enter the string you want:")
s=string("str")
s.get_string()
print(s.str)
s.print_string()
print(s.str)


