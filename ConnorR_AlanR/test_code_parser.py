import code_parser as c

def test_code_parser_HH123():
    assert c.get_db_link("NN-LHH-NNN123-NNN") == "HH-123"

def test_code_parser_too_short():
    assert c.get_db_link("NN-LH-NNN12-NNN") == False

def test_code_parser_way_too_short():
    assert c.get_db_link("NN-LH-NNN12") == False 

