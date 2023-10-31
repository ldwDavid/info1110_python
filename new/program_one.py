'''
Interface of the exam
'''

import setup
import sys

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110'])
    Check command line arguments
    '''
    pass

def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    pass

def main(args):
    '''
    Implement all stages of exam process.
    '''
    pass
    
if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
