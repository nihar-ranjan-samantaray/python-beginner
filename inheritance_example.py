class Father():
    def __init__(self,fathername,fatherage):
        self.fathername = fathername
        self.fatherage = fatherage

    def fatherDetails(self):
        print(f"Fathe's Name is {self.fathername}")
        print(f"Fathe's Age is {self.fatherage}")

class Mother():
    def __init__(self,mothername,motherage):
        self.mothername = mothername
        self.motherage = motherage

    def motherDetails(self):
        print(f"Mother's Name is {self.mothername}")
        print(f"Mother's Age is {self.motherage}")

class Son(Father,Mother):
    
    def sonDetails(self):
        print(f"Father's Name is {self.fathername}")
        print(f"Fathe's Age is {self.fatherage}")
        # print(f"Mother's Name is {self.mothername}")
        # print(f"Mother's Age is {self.motherage}")
        # print(f"Son's Name is {self.sonname}")
        # print(f"Son's Age is {self.sonage}")


fatherObject = Father("Niranjan Samantaray",53)
motherObject = Mother("Manorama Samantaray",45)
sonObject = Son("Niranjan Samantaray",53)
# sonObject.fathername = "Niranjan"
# sonObject.mothername = "Manorama"
# sonObject.fatherage = 58
# sonObject.motherage = 45
# sonObject.sonname = "Nihar"
# sonObject.sonage = "25"
sonObject.sonDetails()