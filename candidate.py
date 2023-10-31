import os


class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        base_time = self.exam.duration if self.exam else 0
        return base_time + self.extra_time
        pass
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        self.sid = sid
        pass

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        self.extra_time = t
        pass
    
    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if self.sid == sid and self.name == name:
            self.confirm_details = True
        pass

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        if not os.path.exists("Submissions"):
            os.makedirs("Submissions")

        with open(f"Submissions/{self.sid}.txt", "a") as file:
            file.write(data + "\n")
        pass
    
    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details:
            self.results = ls
        pass

    def do_exam(self):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        if self.exam:
            data = self.exam.preview_exam()
            self.log_attempt(data)
        else:
            print("No exam available.")
        pass
       
    def __str__(self):
        '''
        You are free to change this, this is here for your debugging convenience.
        '''
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam is None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

