import question

test1 = question.Question("short")

test1.set_type("short")
assert (not test1.set_description(""))
assert (test1.set_description("ABC") is True)
assert (not test1.set_correct_answer("E"))
assert (test1.set_correct_answer("D") is True)
assert (not test1.set_marks("a"))
assert (test1.set_marks(0) is True)
