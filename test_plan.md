# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail 

Table 1: Summary of test cases for method `mark_response` for question type `short`
Question Type: short
Correct Answer: Python
mark: 1

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
|1     | Correct Answer| Python       | 1                |        |
|2     | Incorrect Answer            | C       | 0                |        |
|3     | Case Insensitivity            | python       | 1                |        |

Table 2: Summary of test cases for method `mark_response` for question type `single`
Question Type: single
Correct Answer: A
mark:1

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
| 4        | Correct Choice            | A       | 1                |        |
| 5        | Incorrect Choice            | B       | 0                |        |
| 6        | Case Insensitivity            | a       | 1                |        |

Table 3: Summary of test cases for method `mark_response` for question type `multiple`
Question Type: multiple
Correct Answer: A,B,C
marks: 3

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
| 7        | All Choices Correct            | A,B,C       | 3                |        |
| 8        | Partial Correct Choices (No Wrong Choices)            | A,B       | 2                |        |
|9|Partial Correct Choices (With Wrong Choices)|A,B,D|2| |
|10         | All Choices Incorrect            | D       | 0                |        |
|11|Case Insensitivity|a,b,c|3||

# 
