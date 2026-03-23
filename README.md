# Embedded Test Automation Framework

A Python-based tool to run automated test cases on a simulated embedded system.

---

## Features

- Runs multiple test cases automatically  
- Compares expected vs actual output  
- Shows PASS / FAIL for each test  
- Displays a final summary  

---

## Project Structure

- embedded-test-framework
- src/
- system_under_test.py
- test_runner.py
- reports/
- tests/
- README.md
- equirements.txt

---

## How to Run

python src/test_runner.py

---

## Example Output

Embedded Test Report
--------------------
Test 1: input=120 | expected=ALERT | actual=ALERT | result=PASS  
Test 2: input=20 | expected=NORMAL | actual=NORMAL | result=PASS  

Summary
-------
Total  : 2  
Passed : 2  
Failed : 0  

---

## Test Scenarios

- Temperature > 100 -> ALERT  
- Temperature <= 100 -> NORMAL  

---

## Future Improvements

- Add JSON/CSV test input  
- Save test reports to file  
- Add pytest testing  
- Support multiple systems  

---

