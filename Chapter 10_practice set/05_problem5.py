from random import randint

class Train:
  def __init__(self, trainNo):
    self.trainNo = trainNo

  def book(self, fro, to):
    print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

  def getstatus(self):
    print (f"Train no: {self.trainNo} is scheduled on time")

  def getfare(self, fro , to ):
    print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is Rs:{randint(1000, 2000)}")

t = Train (1122)
t.book ("Karachi","Islamabad")
t.getstatus ()
t.getfare ("Karachi","Islamabad")