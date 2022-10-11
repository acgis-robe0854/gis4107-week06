import doc_scanner as d

def test_has_x_code_exact():
    assert d.has_x_code ("Tx6op3") == True

def test_has_x_code_empty():
    assert d.has_x_code ("") == False 

def test_has_x_code_letters_no_order():
    assert d.has_x_code("Terry xavier 6 oliver peter 3") == False

def test_has_x_code_included():
    assert d.has_x_code("The code is Tx6op3") == True

def test_get_x_code_position_exact():
    assert d.get_x_code_position ("Tx6op3") == 1

def test_get_x_code_position_empty():
    assert d.get_x_code_position ("") == -1 

def test_get_x_code_position_no_order():
    assert d.get_x_code_position ("Terry xavier 6 oliver peter 3") == -1

def test_get_x_code_position_included():
    assert d.get_x_code_position ("The code is Tx6op3") == 13