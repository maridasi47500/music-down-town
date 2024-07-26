from country import Country
from user import User
from job import Job
from couragelog import Couragelog
from couragejournal import Couragejournal
from asif import Asif
from goals import Goals
from fourpointfield import Fourpointfield
from symbol import Symbol
from song import Song
from jobscript import Jobscript


class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Song=Song()
    self.Jobscript =Jobscript()
    self.Job=Job()
    self.Couragelog=Couragelog()
    self.Couragejournal=Couragejournal()
    self.Asif=Asif()
    self.Goals=Goals()
    self.Fourpointfield=Fourpointfield()
    self.Symbol=Symbol()
