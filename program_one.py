'''
Interface of the exam
'''

import setup
import question
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
    questions = []
    while True:
        # Prompt for question type
        qtype = input("Enter question type (short/single/multiple/end): ")

        if qtype == "end":
            break

        if qtype not in ["short", "single", "multiple"]:
            print("Invalid question type. Please enter again.")
            continue

        # Prompt for question description
        description = input("Enter the question description: ")

        # Prompt for correct answer
        correct_answer = input("Enter the correct answer: ")

        # If multiple choice, prompt for answer options
        answer_options = []
        if qtype == "multiple":
            answer_options = input("Enter answer options separated by comma (e.g., A,B,C): ").split(',')

        # Prompt for marks
        marks = int(input("Enter the marks for the question: "))

        # Create a Question object and add to the questions list
        q = question.Question(qtype)
        q.set_description(description)
        q.set_correct_answer(correct_answer)
        q.set_marks(marks)
        if qtype == "multiple":
            q.set_answer_options(answer_options)

        questions.append(q)
        print("Question added successfully!")

    # Optionally, save questions to a file or database for future use
    # ...

    print("All questions entered successfully!")
    pass


if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
