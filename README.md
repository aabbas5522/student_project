# Student App

A small command-line app that takes a student's name and marks, validates them, calculates a grade and prints a report.

## Project structure

```
src/student_app/
├── main.py                  # entry point
├── models/student.py        # Student class
├── services/calculator.py   # grade calculation
├── utils/validation.py      # input validation
└── reports/student_report.py # report output
```

## Run

From the project's top folder:

if you have Python3 installed : 

```bash
python3 -m pip install -r requirements.txt
cd src
python3 -m student_app.main
```

else 


```bash
python -m pip install -r requirements.txt
cd src
python -m student_app.main
```



## Grading scale

| Marks  | Grade |
|--------|-------|
| 80–100 | A     |
| 70–79  | B     |
| 60–69  | C     |
| 50–59  | D     |
| 0–49   | F     |
