import random


class Question:

    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it
        self.qtype = None
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None

    def set_type(self, qtype):
        """
        Update instance variable qtype.
        """
        self.qtype = qtype
        pass

    def set_description(self, desc):
        """
        Update instance variable description.
        """
        if self.qtype == "end":
            return False
        if desc == "":
            return False
        if str(desc) != desc:
            return False
        return True
        pass

    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer.
        """
        if self.qtype == "end":
            return False
        if str(ans) != ans:
            return False
        if self.qtype == "single":
            if ans.upper() not in ["A", "B", "C", "D"]:
                return False
        elif self.qtype == "multiple":
            a = ans.split(",")
            for i in a:
                if i.upper() not in ["A", "B", "C", "D"]:
                    return False
        self.correct_answer = ans
        return True
        pass
    def set_marks(self, num):
        """
        Update instance variable marks.
        """
        if not is_int(num):
            return False
        if int(num) != num:
            return False
        if num < 0:
            return False
        self.marks = num
        pass

    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.

        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        if self.qtype == "short" or self.qtype == "end":
            self.answer_options = opts
            return True
        else:
            if type(opts) != list:
                return False
            for i in opts:
                if type(i) != tuple:
                    return False
                if len(i) != 2:
                    return False
                if str(i[0]) != i[0]:
                    return False
                if type(i[1]) != bool:
                    return False
        a = self.correct_answer.split(",")
        for i in a:
            for j in opts:
                if i == j[0][0]:
                    j[1] = True
        pass

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        if self.qtype == "short" or self.qtype == "end":
            return ""
        else:
            opt_desc = ""
            for i in self.answer_options:
                opt_desc += i[0]
                opt_desc += "\n"
        return opt_desc
        pass
    def mark_response(self, response):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        pass

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        if show:
            if i == 0:
                i = "X"
                pass
            if self.qtype == "end":
                return "-End-"
            else:
                return "Question" + i + "\t" + self.qtype + "Answer" + self.marks + "\n" + \
                       self.description + "\n" + \
                       self.get_answer_option_descriptions() + "\n" + \
                       "Expected Answer:\t" + self.correct_answer + "\n"
        pass

    def generate_order(self):
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.

        Sample usage:
        generate_order()
            [3,1,0,2]
        """
        sou = [0, 1, 2, 3]
        dir = []
        while len(sou) > 1:
            a = random.randint(0, 3)
            if a in sou:
                sou.remove(a)
                dir.append(a)
        dir.append(sou[0])
        return dir

    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """
        a = generate_order()
        options = []
        for i in range(len(self.answer_options)):
            options.append(self.answer_options[a[i]])
        return options
        pass

    def __str__(self):
        """
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        """
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''

    pass

def is_int(i):
    try:
        int(i)
        return True
    except:
        return False
