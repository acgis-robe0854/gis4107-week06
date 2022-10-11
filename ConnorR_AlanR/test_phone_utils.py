import phone_utils as p

def test_is_valid_phone_number_valid():
    assert p.is_valid_phone_number("333-666-9999") == True

def test_is_valid_phone_number_not_number():
    assert p.is_valid_phone_number("33e-666-9999") == False

def test_is_valid_phone_number_too_long():
    assert p.is_valid_phone_number("333-666-99999") == False

def test_is_valid_phone_number_too_short():
    assert p.is_valid_phone_number("333-666-999") == False