#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg
from datetime import timedelta

ISS_API = "http://api.open-notify.org/iss-now.json"

def main():
    
    api_resp = requests.get(ISS_API)
    
    resp_dt = api_resp.json()

    lat = resp_dt['iss_position']['latitude']
    lon = resp_dt['iss_position']['longitude']

    cdt_adj = timedelta(hours=5)

    time_str = datetime.datetime.utcfromtimestamp(resp_dt['timestamp']) - cdt_adj

    loc_dt = rg.search((lat, lon))

    city = loc_dt[0]["name"]
    country = loc_dt[0]["cc"]

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {time_str}")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City/Country: {city}, {country}")

    print("")


if __name__ == "__main__":
    main()
