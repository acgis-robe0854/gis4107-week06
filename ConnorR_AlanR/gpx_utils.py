def get_coords_from_gpx(gpx):
    if "trkpt" not in gpx: 
        return None, None
    parts = gpx.split('"')
    lat = parts[1]
    long = parts[3]
    return float(long),float(lat)
    



print (get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">'))
print(get_coords_from_gpx('lat="45.3888995" lon="-75.7472631"'))
print (get_coords_from_gpx('trkpt lat="45.3888995" lon="-75.7472631">'))