
import os
import re
import configparser as ConfigParser  # py3

def read_token():
    config = ConfigParser.RawConfigParser()
    config.read([
        '.cloudflare.cfg',
        os.path.expanduser('~/.cloudflare.cfg'),
        os.path.expanduser('~/.cloudflare/cloudflare.cfg')
    ])

    try:
        token = re.sub(r"\s+", '', config.get('CloudFlare', 'token'))
    except (ConfigParser.NoOptionError, ConfigParser.NoSectionError):
        token = None

    return token