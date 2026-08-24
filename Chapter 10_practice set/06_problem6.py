from random import randint

class Train:
  def __init__(slf, trainNo): # I will use slf on the place of self to whether something happens or not
    slf.trainNo = trainNo

  def book(nomi, fro, to): # We can use anything on the place of self It will not affect the code but it is good to maintain the readability of the code and use the self
    print(f"Ticket is booked in train no: {nomi.trainNo} from {fro} to {to} ")

  def getstatus(self):
    print (f"Train no: {self.trainNo} is scheduled on time")

  def getfare(self, fro , to ):
    print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is Rs:{randint(1000, 2000)}")

t = Train (1122)
t.book ("Karachi","Islamabad")
t.getstatus ()
t.getfare ("Karachi","Islamabad")
# So using SLF or anything else does not affect the code but it just make code a little less readable So that's why we use self to increase the readability