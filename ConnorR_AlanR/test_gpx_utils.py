import gpx_utils as g

def test_get_coords_from_gpx_good():
    assert g.get_coords_from_gpx('<trkpt lat="45.3888995" lon="-75.7472631">') == (-75.7472631,45.3888995)

def test_getcoord_from_gpx_missing_trkpt():
    assert g.get_coords_from_gpx('lat="45.3888995" lon="-75.7472631"') == (None, None)

def test_get_coords_from_gpx_different_numbers_of_decimals():
    assert g.get_coords_from_gpx('<trkpt lat="45.3888342310995" lon="-75.7631">') == (-75.7631, 45.3888342310995)