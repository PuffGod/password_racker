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
from typing import List, Tuple, Generator
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

def _gen_random_password(password_length:int, characters:str) -> str:
    '''
    generates a random password

    :param int password_length: number of characters in password
    :param str characters: characters to use
    :return: password as a string
    :rtype: str
    '''
    password = list()
    for _ in range(0, password_length):
        rand_idx = random.randrange(0, len(characters))
        password.append(characters[rand_idx])
    return ''.join(password)

def _gen_all_passwords(password_length:int, characters:str) -> Generator:
    '''
    generates all the possible passwords for the combination of characters

    :param int password_length: length of passowrd
    :param str characters: characters to use
    :return: tuples with elements with the password length of strings; the length of the tuples is the
        password length
        e.g. -> (('0', '1', '2', 'r', '\'), (...))
    :rtype: generator of tuples; all elements of tuples are strings
    '''
    return product(characters, repeat = password_length)

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
        passwords_to_crack.append(
            _gen_random_password(
                password_length = password_max_length, 
                characters = characters_to_use
            ) 
        )

    # log passwords created
    logger.info(f'passwrds created to crack -> {", ".join(passwords_to_crack)}')

    return passwords_to_crack

def crack_password(password:str, characters_to_use:str) -> Tuple[bool, str, float]:
    '''
    '''
    number_characters_in_password = [9, 10, 11, 12]

    potential_passwords = _gen_all_passwords(password_length = 2, characters = characters_to_use)

    counter = 0
    for pt_pswd in potential_passwords:
        print(''.join(pt_pswd))

        if counter >= 5:
            break
        counter += 1

    return False, 'TSMA', 0.4

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

    # crack password

    # for password in passwords_to_crack:
    found, found_password, time_to_crack = crack_password(
        password = '12345',
        characters_to_use = characters_to_use
    )
    if found:
        logger.info(f'found password -> {found_password} in {time_to_crack}')

    return None


if __name__ == '__main__':
    main()