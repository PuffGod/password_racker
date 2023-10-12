'''
<file doc string>
'''

'''
packages
'''

import string
import random

from datetime import datetime
from time import perf_counter
from typing import List
from itertools import product

from utilities import set_up_logger
from constants import STRING_DT_FORMAT

'''
logger
'''

import logging
string_dt_now = datetime.now().strftime(STRING_DT_FORMAT)
logger = logging.getLogger()
logger.name = 'cracker'
log_file = f'cracker_{string_dt_now}.log'
log_path = './logs'
set_up_logger(log_path, log_file, logger)

'''
supportive functions
'''

'''
callable functions
'''

def create_passwords(number_to_create:int, password_max_length:int, characters_to_use:str) -> List[str]:
    '''
    creates randomly generated passwords to crack

    :param int number_to_create: number of passwords to create
    :param int password_max_length: max length of password
    :param str characters_to_use: characters to use in password
    :return: passwords created
    :rtype: list
    '''
    # set-up
    passwords_to_crack = list()
    
    # log characters to use
    logger.info(f'characters used in password -> {characters_to_use}')

    # create passwords
    for _ in range(0, number_to_create):
        # create random password
        password = list()
        for _ in range(0, password_max_length):
            rand_idx = random.randrange(0, len(characters_to_use))
            password.append(characters_to_use[rand_idx])
        
        # add to list of passwords
        passwords_to_crack.append(''.join(password))

    # log passwords created
    logger.info(f'passwrds created to crack -> {", ".join(passwords_to_crack)}')

    return passwords_to_crack

'''
main function
'''

def main():
    '''
    '''
    # get ascii characters except for last six which include the <space>, new line, carriage return, etc...
    characters_to_use = string.printable[:-6]

    # create passwords
    passwords_to_crack = create_passwords(
        number_to_create = 100,
        password_max_length = 10,
        characters_to_use = characters_to_use
    )



    return None


if __name__ == '__main__':
    main()