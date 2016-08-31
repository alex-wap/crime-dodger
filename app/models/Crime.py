from system.core.model import Model
from sodapy import Socrata
import time
import datetime

client = Socrata("data.sfgov.org", "8gffbg1meMZ1e2Z0yOz2OpwZq")

class Crime(Model):
  def __init__(self):
    super(Crime, self).__init__()
  def get_crimes(self):
    crimes = client.get("cuks-n6tp", select ="category,time,location,date", where=""" category='ASSAULT'
     or category='VEHICLE THEFT' or category='VANDALISM' or category='KIDNAPPING'
     or category='SEX OFFENSES, FORCIBLE' or category='DRIVING UNDER THE INFLUENCE' and DATE > '2015-01-01T00:00:00.000' """,limit=70)
    for crime in crimes:
      real_time = time.strptime(crime['time'], "%H:%M")
      crime['real_time'] = real_time
    client.close()
    print "this is the data from the set:", real_time
    return crimes
