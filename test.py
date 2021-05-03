import src.pyjsonutils.pyjsonutils as pyjsonutils
x = pyjsonutils.open_file_as_dict("tests/test.json")
f = pyjsonutils.find_key_from_value(x, "test1")

print(pyjsonutils.pretty_print(x))
