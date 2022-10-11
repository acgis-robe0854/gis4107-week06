def is_valid_phone_number(phone_number):
    parts = phone_number.split('-')
    return len(parts[0]) == 3 and parts[0].isdigit() \
        and len(parts[1]) == 3 and parts[1].isdigit() \
        and len(parts[2]) == 4 and parts[2].isdigit()

print(is_valid_phone_number("333-666-9999"))