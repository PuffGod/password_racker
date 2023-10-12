'''
<file doc string>
'''

'''
packages
'''

from datetime import datetime
from time import perf_counter
from typing import List

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

def create_passwords(number_to_create:int) -> List[str]:
    '''
    '''

    return None

'''
main function
'''

def main():
    '''
    '''
    return None


if '__name__' == "__main__":
    main()