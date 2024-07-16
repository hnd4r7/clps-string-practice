def extract_number(x: str) -> str:
    num_str = ""
    for i, c in enumerate(x):
        if c.isdigit():
            num_str = x[i:]
            break
    if not num_str:
        return ""
    elif '.' not in num_str:
        return num_str + '.00'
    else:
        dot_index = num_str.index('.')
        int_part = num_str[:dot_index]
        decimal_part = num_str[dot_index + 1:]
        if len(decimal_part) > 2:
            decimal_part = decimal_part[:2]
        return int_part + '.' + decimal_part

assert extract_number("abcd") == ""
assert extract_number("abcd123.456") == "123.45"
assert extract_number("abcd123") == "123.00"