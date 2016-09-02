from sodapy import Socrata

# client = Socrata("sandbox.demo.socrata.com", None)
# print client.get("nimj-3ivp", limit=10)

# client = Socrata("data.cms.gov/", None)
# print client.get("97k6-zzx3", limit=10)
# https://resource/97k6-zzx3.json?$limit=5

client = Socrata("data.sfgov.org", "8gffbg1meMZ1e2Z0yOz2OpwZq")
#client.get("cuks-n6tp", limit=1)
assault = client.get("cuks-n6tp", select ="category,time,location", where ="category='ASSAULT'",limit=10)
print "assault data"
print assault
theft = client.get("cuks-n6tp", select ="category,time,location", where ="category='VEHICLE THEFT'",limit=10)
print "vehicle theft data"
print theft
vandalism = client.get("cuks-n6tp", select ="category,time,location", where ="category='VANDALISM'",limit=10)
print "VANDALISM data"
print vandalism
kidnapping = client.get("cuks-n6tp", select ="category,time,location", where ="category='KIDNAPPING'",limit=10)
print "KIDNAPPING data"
print kidnapping
sex = client.get("cuks-n6tp", select ="category,time,location", where ="category='SEX OFFENSES, FORCIBLE'",limit=10)
print "SEX OFFENSES, FORCIBLE data"
print sex
dui = client.get("cuks-n6tp", select ="category,time,location", where ="category='DRIVING UNDER THE INFLUENCE'",limit=10)
print "DUI data"
print dui
client.close()

# search radius
# https://data.sfgov.org/resource/cuks-n6tp.json?$where=within_circle(location,%2037.78,%20-122.41,%201000)

# https://data.cms.gov/resource/97k6-zzx3.json?$limit=5
# client = Socrata("https://data.cms.gov/resource/", None)
# print client.get("http://data.cms.gov/resource/97k6-zzx3.json?$order=average_covered_charges$limit=1", limit=2)

# app token - need it eventually
# https://data.seattle.gov/resource/3k2p-39jp.json?$$app_token=APP_TOKEN
# https://dev.socrata.com/docs/app-tokens.html
# 8gffbg1meMZ1e2Z0yOz2OpwZq
# secret token at https://data.sfgov.org/profile/alex-wap/7wfp-cp8m/app_tokens
'''
SF DATA FORMAT
location.coordinates
LONG , LAT
-122.493328, 37.764731
GOOGLE DATA FORMAT
LAT, LONG
37.764731, -122.493328

latitude is 0 at equator, -90 south pole, 90 north pole
longitude is 0 at Greenwich Meridian, -180 is west, 180 is east.

Python for SODA
https://github.com/xmunoz/sodapy

SELECT
category
time
location

WHERE
where="category='ASSAULT' 
or category='VEHICLE THEFT' 
or category='VANDALISM' 
or category='KIDNAPPING' 
or category='SEX OFFENSES, FORCIBLE'
or category='DRIVING UNDER THE INFLUENCE'"

time is stored as text...

API END POINT
 https://data.sfgov.org/resource/cuks-n6tp.json

LEARN SoQL queries
https://dev.socrata.com/foundry/data.sfgov.org/cuks-n6tp
https://dev.socrata.com/docs/filtering.html
https://dev.socrata.com/docs/queries/

SELECT
WHERE
ORDER BY
GROUP BY
LIMIT
OFFSET

'''