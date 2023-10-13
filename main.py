'''
<file doc string>
'''

'''
packages
'''

import string
import random

from datetime import datetime, timedelta
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

def crack_password_brute_force(password:str, characters_to_use:str) -> Tuple[bool, str, float, int]:
    '''
    uses brute for method to crack password

    :param str password: password to crack
    :param str characters_to_use: ascii characters to use
    :return: flag if fournd, the original password and the time to crack in seconds
        tuple[0] -> bool; True if found, False if not found
        tuple[1] -> string; original password
        tuple[2] -> float; time to crack in seconds
        tuple[3] -> int; number of guesses used
    :rtype: tuple
    '''
    # set-up
    bool_return = False

    # generate all passowrds
    potential_passwords = _gen_all_passwords(
        password_length = len(password), characters = characters_to_use
    )
    logger.info('generated all potential passwords')

    # brute force crack
    logger.info('starting to crack password')
    start_time = perf_counter()
    counter = 1
    for pt_pswd in potential_passwords:
        # get string from tuple
        pwd = ''.join(pt_pswd)

        # compare password
        if pwd == password:
            stop_time = perf_counter()
            bool_return = True
            break
        
        counter += 1

    logger.info('finished cracking password')

    return bool_return, password, stop_time - start_time, counter

def crack_password_random_selection(password:str, characters_to_use:str, max_time:int) -> Tuple[bool, str, float, int]:
    '''
    uses random guess to attempt to crack password; if not cracked in perscribed time give up and get new
    password

    :param str password: password to crack
    :param str characters_to_use: ascii characters to use
    :param int max_time: maximum allowable time, in minutes, to try to crack a password
    :return: flag if fournd, the original password and the time to crack in seconds
        tuple[0] -> bool; True if found, False if not found
        tuple[1] -> string; original password
        tuple[2] -> float; time to crack in seconds
        tuple[2] -> int; guess count
    :rtype: tuple
    '''
    # set-up
    bool_return = False
    td_max_time = timedelta(minutes = max_time)
    dt_start = datetime.now()
    keep_guessing = True
    
    # start guessing
    logger.info('starting to guess using random selection')
    start_time = perf_counter()
    counter = 1

    while datetime.now() - dt_start < td_max_time and keep_guessing:
        password_guess = _gen_random_password(
            password_length = len(password),
            characters = characters_to_use
        )

        # test if guessed correct
        if password_guess == password:
            stop_time = perf_counter()
            bool_return = True
            keep_guessing = False
            logger.info('found password by random guessing')
            break

        counter += 1
    
    if not bool_return:
        stop_time = perf_counter()

    return bool_return, password, stop_time - start_time, counter

def results(found:bool, password:str, time:float, guess_count:int):
    '''
    prints results to log and screen

    :param bool found: flag if password is cracked
    :param str password: password trying to crack
    :param int guess_count: number of guesses to crack password
    :return: None
    '''
    if found:
        logger.info(f'found password -> {password} in {time:5f} seconds used {guess_count:,} guesses')
    else:
        logger.error(f'did not find password -> {password} in {time:5f} seconds used {guess_count:,} guesses')    
    
    return None

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

    # crack password using brute force
    found, found_password, time_to_crack, guess_count = crack_password_brute_force(
        password = '12345',
        characters_to_use = characters_to_use
    )

    # print results
    results(found = found, password = found_password, time = time_to_crack, guess_count = guess_count)

    # crack password through random guessing
    found, found_password, time_to_crack, guess_count = crack_password_random_selection(
        password = '12',
        characters_to_use = characters_to_use,
        max_time = 1
    )

    # print results
    results(found = found, password = found_password, time = time_to_crack, guess_count = guess_count)

    return None


if __name__ == '__main__':
    main()