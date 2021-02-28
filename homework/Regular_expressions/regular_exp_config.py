import re


with open("Python-Enchantress10/homework/Regular_expressions/config.ini") as config_file:
    pattern = r"\(?P<key_word>(_secret)|(_key)|(.password)) = (?P<secret_word>[*\w\-\.]+)$"
    file = config_file.read()
    res = re.sub(pattern, "(?P<key_word>(_secret)|(_key)|(.password)) = (?P<secret_word>[xxxxx]+)$", file)
    print(res)
