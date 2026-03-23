from system_under_test import check_temperature


TEST_CASES = [
    {"test_id": 1, "input": 120, "expected": "ALERT"},
    {"test_id": 2, "input": 20, "expected": "NORMAL"},
    {"test_id": 3, "input": 101, "expected": "ALERT"},
    {"test_id": 4, "input": 100, "expected": "NORMAL"},
    {"test_id": 5, "input": -10, "expected": "NORMAL"},
    {"test_id": 6, "input": 250, "expected": "ALERT"},
]


def run_single_test(test_case: dict) -> dict:
    """
    Run one test case and return the result.
    """
    actual = check_temperature(test_case["input"])
    expected = test_case["expected"]
    result = "PASS" if actual == expected else "FAIL"

    return {
        "test_id": test_case["test_id"],
        "input": test_case["input"],
        "expected": expected,
        "actual": actual,
        "result": result,
    }


def run_tests() -> None:
    """
    Run all temperature test cases and print results.
    """
    results = []
    passed = 0
    failed = 0

    print("Embedded Test Report")
    print("--------------------")

    for test_case in TEST_CASES:
        test_result = run_single_test(test_case)
        results.append(test_result)

        if test_result["result"] == "PASS":
            passed += 1
        else:
            failed += 1

        print(
            f"Test {test_result['test_id']}: "
            f"input={test_result['input']} | "
            f"expected={test_result['expected']} | "
            f"actual={test_result['actual']} | "
            f"result={test_result['result']}"
        )

    print("\nSummary")
    print("-------")
    print(f"Total  : {len(results)}")
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")


if __name__ == "__main__":
    run_tests()