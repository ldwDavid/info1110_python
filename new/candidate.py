class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        if self.exam:
            return self.exam.duration + self.extra_time
        return 0
            
    def edit_sid(self, sid):
        if sid.isdigit() and len(sid) == 9:
            self.sid = sid
            return True
        return False

    def edit_extra_time(self, t):
        if isinstance(t, int) and t >= 0:
            self.extra_time = t
            return True
        return False
    
    def set_confirm_details(self, sid, name):
        if self.name == name and self.sid == sid:
            self.confirm_details = True

import os

class Candidate:
    # ... (other methods and attributes)

    def log_attempt(self):
        if self.confirm_details:
            submissions_directory = "Submissions"
            if not os.path.exists(submissions_directory):
                os.makedirs(submissions_directory)
            file_path = os.path.join(submissions_directory, f"{self.sid}.txt")
            with open(file_path, "w") as file:
                for i, response in enumerate(self.results, start=1):
                    file.write(f"Question {i} - Response: {response}\n")

            print(f"Responses saved in {file_path}")

        else:
            print("Candidate details are not confirmed. Cannot save responses.")


    
    def set_results(self, ls):
        if self.confirm_details:
            self.results = ls
        pass
def do_exam(self, preview=False):
    if not self.exam:
        return

    if not preview:
        print(f"Candidate: {self.name}({self.sid})")
        print(f"Exam duration: {self.get_duration()} minutes")
        print(f"You have {self.get_duration()} minutes to complete the exam.")

    for i, question in enumerate(self.exam.questions[:-1], start=1):
        print(f"Question {i}:")
        if not preview:
            print(question.preview_question(i))

        if not preview:
            candidate_answer = input("Your Answer: ").strip()

            if question.qtype == "single":
                valid_responses = ["A", "B", "C", "D"]
                while candidate_answer not in valid_responses:
                    print("Invalid Answer: Please enter A, B, C, or D.")
                    candidate_answer = input("Your Answer: ").strip().upper()
            elif question.qtype == "multiple":
                valid_responses = ["A", "B", "C", "D"]
                candidate_answer = input("Your Answer (comma-separated, e.g., A, B): ").strip().upper()
                while not all(response in valid_responses for response in candidate_answer.split(", ")):
                    print("Invalid Answer: Please enter one or more of A, B, C, or D, separated by commas.")
                    candidate_answer = input("Your Answer (comma-separated, e.g., A, B): ").strip().upper()
            else:
                candidate_answer = input("Your Answer: ").strip()

            self.results.append(candidate_answer)
            marks = question.mark_response(candidate_answer)
            print(f"You have scored {marks:.2f} marks for this question.\n")

    if not preview:
        self.log_attempt(self.results)

       
    def __str__(self):
        '''
        You are free to change this, this is here for your debugging convenience.
        '''
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

