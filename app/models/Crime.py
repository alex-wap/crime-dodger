from system.core.model import Model
from sodapy import Socrata

client = Socrata("data.sfgov.org", "8gffbg1meMZ1e2Z0yOz2OpwZq")

class Crime(Model):
  def __init__(self):
    super(Crime, self).__init__()
  def get_crimes(self):
    crimes = client.get("cuks-n6tp", select ="category,time,location", where="""category='ASSAULT' 
      or category='VEHICLE THEFT' or category='VANDALISM' or category='KIDNAPPING' 
      or category='SEX OFFENSES, FORCIBLE' or category='DRIVING UNDER THE INFLUENCE'""",limit=30)
    client.close()
    return crimes