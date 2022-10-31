import dms_converter as d
def test_dms2dd_e_n ():
    assert d.dms2dd("075 45 03 E 50 23 05 N") == ('75.7508', '50.3847')

def test_dms2dd_w_n ():
    assert d.dms2dd("075 45 03 W 50 23 05 N") == ('-75.7508', '50.3847')

def test_dms2dd_w_s ():
    assert d.dms2dd("075 45 03 W 50 23 05 S") == ('-75.7508', '-50.3847')

def test_dms2dd_lon_too_large ():
    assert d.dms2dd("500 45 03 W 50 23 05 N") == (None, None)

def test_dms2dd_lat_too_large ():
    assert d.dms2dd("075 45 03 W 99 23 05 N") == (None, None)