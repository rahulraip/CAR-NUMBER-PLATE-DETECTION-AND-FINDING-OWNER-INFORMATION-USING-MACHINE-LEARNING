#! /usr/bin/python3



import cgi
import requests
import xmltodict
import json

print("content-type:text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")

def get_vehicle_info(plate_number):
    print(plate_number)
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={}&username=usertest1".format(str(plate_number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1
print(get_vehicle_info(cmd))
