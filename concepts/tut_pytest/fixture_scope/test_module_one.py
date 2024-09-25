# test_module_one.py

def test_func_one(function_fixture, module_fixture, session_fixture):
    function_fixture["counter"] += 1
    module_fixture["counter"] += 1
    session_fixture["counter"] += 1
    
    assert function_fixture["counter"] == 1   # Resets for each function
    assert module_fixture["counter"] == 1     # First increment in module
    assert session_fixture["counter"] == 1    # First increment in session

class TestClassOne:
    def test_func_two(self, function_fixture, class_fixture, module_fixture, session_fixture):
        function_fixture["counter"] += 1
        class_fixture["counter"] += 1
        module_fixture["counter"] += 1
        session_fixture["counter"] += 1

        assert function_fixture["counter"] == 1   # Resets for each function
        assert class_fixture["counter"] == 1      # First increment in class
        assert module_fixture["counter"] == 2     # Continues from previous function test
        assert session_fixture["counter"] == 2    # Continues from previous function test

    def test_func_three(self, function_fixture, class_fixture, module_fixture, session_fixture):
        function_fixture["counter"] += 1
        class_fixture["counter"] += 1
        module_fixture["counter"] += 1
        session_fixture["counter"] += 1

        assert function_fixture["counter"] == 1   # Resets for each function
        assert class_fixture["counter"] == 2      # Class retains state
        assert module_fixture["counter"] == 3     # Continues from previous tests
        assert session_fixture["counter"] == 3    # Continues from previous tests

def test_func_four(function_fixture, module_fixture, session_fixture):
    function_fixture["counter"] += 1
    module_fixture["counter"] += 1
    session_fixture["counter"] += 1

    assert function_fixture["counter"] == 1   # Resets for each function
    assert module_fixture["counter"] == 4     # Continues from previous tests
    assert session_fixture["counter"] == 4    # Continues from previous tests
