import question


# Test set_type method
def test_set_type():
    test_question = question.Question("short")
    assert test_question.set_type("short") is True
    assert test_question.set_type("single") is True
    assert test_question.set_type("multiple") is True
    assert test_question.set_type("end") is True
    assert not test_question.set_type("invalid_type")


# Test set_description method
def test_set_description():
    test_question = question.Question("short")
    assert test_question.set_description("This is a valid description") is True
    assert not test_question.set_description("")
    test_question.set_type("end")
    assert not test_question.set_description("This should fail for 'end' type")


# Test set_correct_answer method
def test_set_correct_answer():
    test_question = question.Question("short")

    test_question.set_type("single")
    assert test_question.set_correct_answer("A") is True
    assert not test_question.set_correct_answer("E")  # Invalid option
    assert test_question.set_correct_answer("B") is True
    test_question.set_type("multiple")
    assert test_question.set_correct_answer("A,B,C") is True
    assert not test_question.set_correct_answer("A,E")  # E is invalid


# Test set_marks method
def test_set_marks():
    test_question = question.Question("short")
    assert test_question.set_marks(1) is True
    assert test_question.set_marks(0) is True
    assert not test_question.set_marks(-1)  # Negative marks
    assert not test_question.set_marks("a")  # Non-integer value


# Main execution block
if __name__ == "__main__":
    print("Test Program for Exam System")
    print("1. Run all tests")
    print("2. Test set_type method")
    print("3. Test set_description method")
    print("4. Test set_correct_answer method")
    print("5. Test set_marks method")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        test_set_type()
        test_set_description()
        test_set_correct_answer()
        test_set_marks()
        print("All tests executed successfully!")
    elif choice == "2":
        test_set_type()
        print("test_set_type executed successfully!")
    elif choice == "3":
        test_set_description()
        print("test_set_description executed successfully!")
    elif choice == "4":
        test_set_correct_answer()
        print("test_set_correct_answer executed successfully!")
    elif choice == "5":
        test_set_marks()
        print("test_set_marks executed successfully!")
    elif choice == "6":
        print("Exiting...")
    else:
        print("Invalid choice!")
