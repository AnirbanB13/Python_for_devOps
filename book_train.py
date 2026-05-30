import dataclasses
from random import randint

class Train():

    def __init__(self, trainNo):
        self.trainNo = trainNo  

    def book(self, fro, to):
        print(f"Ticket is booked in {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Ticket is booked in {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is booked in {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

    
train = Train(12339)
train.book("Rampur", "Delhi")
train.getStatus()
train.getFare("Rampur", "Delhi")