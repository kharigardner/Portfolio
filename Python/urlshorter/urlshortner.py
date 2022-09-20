# this module is used to shorten the url and output the shortened url

# import the modules
import os
import re
import random
import string
import hashlib
import sys

# creating classes for the urlshortner

class UrlShortner:
    def __init__(self):
        pass
    @staticmethod
    def shorten_url(url):
        with url as f:
            assert isinstance(f, str)
            # creating a hash for the url
            hash_object = hashlib.md5(f.encode())
            # converting the hash to hexadecimal
            hex_dig = hash_object.hexdigest()
            # creating a random string of 6 characters
            rand_string = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            # combining the hexadecimal and the random string
            return hex_dig + rand_string
    @staticmethod
    def get_url(short_url):
        with short_url as f:
            assert isinstance(f, str)
            # splitting the string into two parts
            hex_dig, rand_string = f.split('_')
            # combining the hexadecimal and the random string
            return hex_dig + rand_string

def urlshortnerfunc(url):
    short_url = UrlShortner.shorten_url(url)
    print(f"Shortened url is: {short_url}")
    get_url = UrlShortner.get_url(short_url)
    print(f"Original url is: {get_url}")
    # opening the url in the default browser
    sys.exit(os.system(f"start {get_url}"))

# command line function
def main():
    url = sys.argv[1]
    # raising an error if the url is not valid
    if not re.match(r'^(?:http|ftp)s?://', url):
        raise ValueError('Invalid URL')
    urlshortnerfunc(url)