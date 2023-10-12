'''
<file doc string>
'''

'''
packages
'''

import string

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

def create_passwords(number_to_create:int, password_max_length:int) -> List[str]:
    '''
    '''
    characters_to_use = string.printable
    print(characters_to_use)

    return None

'''
main function
'''

def main():
    '''
    '''
    create_passwords()
    return None


if '__name__' == "__main__":
    main()