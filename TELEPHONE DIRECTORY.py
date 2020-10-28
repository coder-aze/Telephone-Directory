class telephone_directory:
    adres=r"C:\Users\ANONYMOUS\Desktop\contact.txt"
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def add(self):
        with open(telephone_directory.adres,"a+",encoding="utf-8") as file:
            file.write(self.name+":  "+str(self.number)+"\n")
    @staticmethod
    def order():
        with open(telephone_directory.adres,"r",encoding="utf-8") as file:
            for x in file:
                print(x,end="")
    @staticmethod
    def remove():
        depo=[]
        with open(telephone_directory.adres,"r",encoding="utf-8") as file:
            result=file.readlines()
            name=input("Name: ")
        with open(telephone_directory.adres,"w+",encoding="utf-8") as file:
            for x in result:
                if x.split(": ")[0].lower()!=name.lower():
                    file.write(x)
                else:
                    depo.append("x")
            if len(depo)==0:
                print("FILE NOT FOUND")
                depo=[]
            else:
                print("NAME HAS DELETED...")
                depo=[]
    @staticmethod
    def filter():
        with open(telephone_directory.adres,"r",encoding="utf-8") as file:
            result=file.readlines()
            start=input("First Letters: ")
            for x in result:
                if x.split(": ")[0].lower().startswith(start.lower()):
                    print(x,end="")
while True:
    print("----------------------------------------------")
    answer=input("1=ADD 2=ORDER 3=REMOVE 4=FILTER: ")
    if answer=="1":
        name=input("name: ")
        try:
            num=int(input("number: "))
            test=telephone_directory(name,num)
            test.add()
        except ValueError:
            print("the number must be numbers")
        """test=telephone_directory(name,num)
        test.add()"""
    elif answer=="2":
        telephone_directory.order()
    elif answer=="3":
        telephone_directory.remove()
    elif answer=="4":
        telephone_directory.filter()
    else:
        print("TRY AGAIN...")

        