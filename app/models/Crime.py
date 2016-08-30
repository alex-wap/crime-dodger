from system.core.model import Model
from sodapy import Socrata
import time
import datetime

client = Socrata("data.sfgov.org", "8gffbg1meMZ1e2Z0yOz2OpwZq")

class Crime(Model):
  def __init__(self):
    super(Crime, self).__init__()
  def get_crimes(self):
    crimes = client.get("cuks-n6tp", select ="category,time,location", where="""category='ASSAULT' 
      or category='VEHICLE THEFT' or category='VANDALISM' or category='KIDNAPPING' 
      or category='SEX OFFENSES, FORCIBLE' or category='DRIVING UNDER THE INFLUENCE' """,limit=10)
    for crime in crimes:
      real_time = time.strptime(crime['time'], "%H:%M")
      # formatted_time = datetime.mktime('%H:%M',real_time)
      #print type(real_time)
      #print type(formatted_time)
      #print type(crime['time'])
      crime['real_time'] = real_time
    client.close()
    return crimes