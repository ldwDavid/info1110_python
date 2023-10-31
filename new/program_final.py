'''
Interface of the exam
'''

import setup
import sys
import program_two
def main(args):
    exam = setup_exam() 
    if exam is None:
        print("Exam setup failed. Exiting.")
        return
    
    print("Welcome to the exam program!")
    while True:
        sid = input("Enter your Student Identification Number (SID): ")
        if not is_valid_sid(sid):
            print("Invalid SID.")
            continue
        
        if sid not in exam.candidate_list:
            print("Candidate number not found for exam.")
            choice = input("Do you want to try again [Y|N]? ").strip().lower()
            if choice != "y":
                print("Exiting.")
                return
        else:
            candidate = get_candidate_by_sid(exam.candidate_list, sid)
            if verify_candidate_details(candidate):
                print("Verifying candidate details...")
                administer_exam(candidate, exam)
            else:
                print("Name does not match records.")

