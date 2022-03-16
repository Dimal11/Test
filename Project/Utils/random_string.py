import random
import string


class RandomString:

    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        rand_string = ''.join(random.sample(letters, 8))
        return rand_string
