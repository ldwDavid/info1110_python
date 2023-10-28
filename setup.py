"""
Functions to setup the exam questions and candidate list for the exam.
"""
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    pass


def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    pass

def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    pass
