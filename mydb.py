from country import Country
from user import User
from job import Job
from symbol import Symbol
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Job=Job()
    self.Symbol=Symbol()
