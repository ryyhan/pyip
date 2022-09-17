import sys
import re
import geocoder
import ipapi
import folium
import pyfiglet as figlet



res= figlet.figlet_format("PYIP Scanner")
print(res)

if(len(sys.argv)==2):
    IP=sys.argv[1]
else:
    IP=0

def main():
    global IP
    if(is_valid_arg(IP)==True):
        if(is_valid_ip(IP)==True):
            output()
            map()


def is_valid_arg(IP):
    if(len(sys.argv)==2):
        return(True)
    else:
        sys.exit("Invalid Number of arguments")


def is_valid_ip(IP):
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if(re.search(regex,IP) and ip_location(IP)!=[]):
        return(True)
    else:
        sys.exit("Invalid ip....exiting!")


def ip_location(IP):
    coords=geocoder.ip(IP)
    return(coords.latlng)


def ip_details(IP):
    info=ipapi.location(ip=IP)
    return(info)


def output():
    global IP
    lat,lang=ip_location(IP)
    print("LAT: ",lat)
    print("LONG: ",lang)

    info=ip_details(IP)
    print("Network :",info["network"])
    print("Version :",info["version"])
    print("City :",info["city"])
    print("Region :",info["region"])
    print("Country :",info["country_name"])
    print("Organization :",info["org"])
    print("Postal :",info["postal"])
    print("Timezone :",info["timezone"])

def map():
    global IP
    loc=ip_location(IP)
    map=folium.Map(location=loc,zoom_start=15)
    folium.Marker(location=loc).add_to(map)
    map.save("map.html")

if __name__=="__main__":
    main()