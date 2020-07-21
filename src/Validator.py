import re


class Validator:
    @staticmethod
    def is_valid(password):
        pattern = r'[A-Za-z0-9@#$%^&+=]{8,}'
        return re.match(pattern, password)
