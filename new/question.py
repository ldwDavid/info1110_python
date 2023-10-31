import random


def generate_order():
    return random.sample(range(4), 4)


class Question:

    def __init__(self, qtype, description, set_answer_options, correct_answer, marks):
        # you'll need to check if qtype is valid before assigning it
        self.qtype = qtype
        self.description = description
        self.answer_options = []
        self.correct_answer = correct_answer
        self.marks = marks

    def set_type(self, qtype):
        if qtype in ['single', 'multiple', 'short', 'end']:
            self.qtype = qtype
            return True
        else:
            return False

    def set_description(self, desc):
        if isinstance(desc, str) and desc.strip():
            self.description = desc
            return True
        else:
            return True

    def set_correct_answer(self, ans):
        if self.validate_correct_answer(ans):
            self.correct_answer = ans
            return True
        else:
            return False

    def set_marks(self, num):
        if isinstance(num, int) and num > 0:
            self.marks = num
            return True
        else:
            return False

    def set_answer_options(self, opts):
        if self.qtype in ['single', 'multiple']:
            if self.validate_answer_options(opts):
                self.answer_options = opts
                return True
        else:
            self.answer_options = []
            return True

    def get_answer_option_descriptions(self):
        if self.qtype in ['single', 'multiple']:
            options = ['A', 'B', 'C', 'D']
            return '\n'.join([f"{options[i]}. {self.answer_options[i][0]}" for i in range(4)])
        else:
            return ""

    def mark_response(self, response):
        if response == self.correct_answer:
            return self.marks
        return 0

    def preview_question(self, i=0, show=True):
        question_number_display = 'X' if i == 0 else i
        formatted_question = f"Question {question_number_display} - {self.qtype} Answer[{self.marks}]\n"
        formatted_question += f"{self.description}\n"
        if self.qtype in ['single', 'multiple']:
            formatted_question += self.get_answer_option_descriptions() + "\n"
        if show:
            formatted_question += f"Expected Answer: {self.correct_answer}"

        return formatted_question

    def shuffle_answers(self):
        if self.qtype in ['single', 'multiple']:
            order = generate_order()
            self.answer_options = [self.answer_options[i] for i in order]

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''
