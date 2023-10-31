"""
Functions to setup the exam questions and candidate list for the exam.
"""
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper) -> list:
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
    questions_list = []
    for line in fobj:
        # Assuming each question is separated by a line break
        if line.strip() == "":
            continue

        qtype = line.strip()
        description = next(fobj).strip()
        possible_answers = next(fobj).strip().split(',')
        expected_answer = next(fobj).strip()
        marks = int(next(fobj).strip())

        # Create a question object
        q = question.Question(qtype)
        q.set_description(description)
        q.set_correct_answer(expected_answer)
        q.set_marks(marks)
        answer_opts = [(opt, False) for opt in possible_answers]
        q.set_answer_options(answer_opts)

        questions_list.append(q)

    # Add an end question
    end_question = question.Question("end")
    questions_list.append(end_question)

    return questions_list
    pass


def sort(to_sort: list, order: int = 0) -> list:
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
    if order == 0:
        return to_sort
    elif order == 1:
        return sorted(to_sort)
    elif order == 2:
        return sorted(to_sort, reverse=True)
    else:
        raise ValueError("Invalid order value. It should be 0, 1, or 2.")
    pass


def extract_students(fobj: io.TextIOWrapper) -> list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    students_list = []
    next(fobj)  # Explicitly skip the header line

    for line in fobj:
        sid, name, extra_time = line.strip().split(',')
        extra_time = int(extra_time) if extra_time else 0  # Convert extra_time to int or default to 0

        # Create a candidate object
        student = candidate.Candidate(sid, name, extra_time)
        students_list.append(student)

    return sort(students_list,1)
    pass
