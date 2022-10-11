def has_x_code (in_text):
    return in_text.find("Tx6op3") != -1

def get_x_code_position (in_text):
    code_position = in_text.find("Tx6op3")
    if code_position != -1:
        return code_position + 1
    else:
        return code_position

print (has_x_code("Terry xavier 6 oliver peter 3"))