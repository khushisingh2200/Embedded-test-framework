# Architecture Overview

The Embedded Test Automation Framework executes predefined test cases on a simulated embedded system and validates the results.

## Workflow

```text
+-------------------------------+
| Input Test Cases              |
|-------------------------------|
| test_id                       |
| input                         |
| expected_output               |
+---------------+---------------+
                |
                v
+-------------------------------+
| Test Runner                   |
|-------------------------------|
| src/test_runner.py            |
|                               |
| - Load test cases             |
| - Execute each test           |
| - Compare expected vs actual  |
| - Mark PASS / FAIL            |
| - Count passed / failed       |
+---------------+---------------+
                |
                v
+-------------------------------+
| System Under Test             |
|-------------------------------|
| src/system_under_test.py      |
|                               |
| - Simulated embedded logic    |
| - Example: temperature check  |
| - Returns system response     |
+---------------+---------------+
                |
                v
+-------------------------------+
| Report Generation             |
|-------------------------------|
| - Terminal report             |
| - PASS / FAIL per test        |
| - Final test summary          |
+-------------------------------+