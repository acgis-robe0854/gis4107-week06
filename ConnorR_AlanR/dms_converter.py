def dms2dd(dms):
    dms = dms.split(" ")
    d_lon = int(dms[0])
    m_lon = int(dms[1])
    s_lon = int(dms[2])
    d_lat = int(dms[4])
    m_lat = int(dms[5])
    s_lat = int(dms[6])
    if d_lon >= 0 and d_lon <= 180 and m_lon >= 0 and m_lon <=59 and s_lon >= 0 and s_lon <=59:
        if dms[3] == "W" or dms[3] == "w":
            lon = f'{-(d_lon +(m_lon/60) + (s_lon/3600)):.4f}'
        else:
            lon = f'{d_lon +(m_lon/60) + (s_lon/3600):.4f}'
    else: 
        return None, None
    if d_lat >= 0 and d_lat <= 90 and m_lat >= 0 and m_lat <=59 and s_lat >= 0 and s_lat <=59:
        if dms[7] == "S" or dms[7] == "s":
            lat = f'{-(d_lat +(m_lat/60) + (s_lat/3600)):.4f}'
        else:
            lat = f'{d_lat +(m_lat/60) + (s_lat/3600):.4f}'
    else: 
        return None, None
    return lon, lat







print(dms2dd("075 45 03 E 50 23 05 N"))
