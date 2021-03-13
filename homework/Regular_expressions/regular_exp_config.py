import re

CONFIG = "./config.ini"
PATTERN = r"\(?P<key_word>(secret)|(key)|(password)) = (?P<secret_word>[*\w\-\.]+)$"


def replace(config):
    with open(config, "w+") as config_file:
        # pattern = r"\(?P<key_word>(_secret)|(_key)|(.password)) = (?P<secret_word>[*\w\-\.]+)$"
        replace_pattern = "xxxxx"
        file = config_file.read()
        for pattern in file:
            result = re.findall(pattern, file, flags=re.M)
            file = re.sub(result, replace_pattern, file)
        return file


if __name__ == "__main__":
    print(replace(CONFIG))

