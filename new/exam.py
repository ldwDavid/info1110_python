class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.name = self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam.
        """
        # you'll need to add some code here
        a = path.split("/")
        name = a[len(a) - 1]
        name.replace(" ", "_")
        return name

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        name = self.name
        return name.replace("_", " ")  # danger! this may replace the origin _ into space
        pass

    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if not self.questions:
            return False
        else:
            self.exam_status = True
            return True
        pass

    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if t > 0:
            self.duration = t
            return True
        return False
        pass

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        if ls[len(ls) - 1].qtype != "end":
            return False
        for h in range(len(ls)):
            i = ls[h]
            if i.discription == "":
                print("Description missing")
                return False
            a = 0
            b = i.answer_options
            c = i.correct_answer.split(",")
            for j in b:
                a += j[1]
            if a == 0:
                print("Correct answer missing")
                return False
            if i.qtype == "single" or i.qtype == "multiple":
                for j in b:
                    if j[0][0] in c:
                        c.remove(j[0][0])
                        pass
                    pass
                if len(c) > 0:
                    print("Answer options incorrect quantity")
                    return False
            if i.qtype == "short":
                if i.answer_options:
                    print("Answer options should not exist")
                    return False
            if i.qtype == "end":
                if h != len(ls) - 1:
                    print("End marker missing or invalid")
                    return False
            self.questions.append(i)
            pass
        return True
        pass

    def preview_exam(self):
        """
        Returns a formatted string.
        """
        pview = ""
        for i in range(len(self.questions)):
            pview += self.questions[i].preview_question(i, True)
            pview += "\n"
        return pview
        pass

    def __str__(self):
        pass

