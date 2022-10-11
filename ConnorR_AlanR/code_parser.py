def get_db_link(building_code):
    short_code = building_code[4:6] + '-' + building_code [10:13]
    code = short_code.split('-')
    check = len(code[0]) == 2 and code[0].isalpha() and len(code[1]) == 3 and code[1].isdigit()
    if check:
        return short_code
    else:
        return check 


