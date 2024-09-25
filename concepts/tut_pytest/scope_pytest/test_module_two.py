# test_module_two.py

def test_func_five(function_fixture, module_fixture, session_fixture):
    function_fixture["counter"] += 1
    module_fixture["counter"] += 1
    session_fixture["counter"] += 1

    assert function_fixture["counter"] == 1   # Resets for each function
    assert module_fixture["counter"] == 1     # Resets for a new module
    assert session_fixture["counter"] == 5    # Continues from previous session state (4 + 1)

class TestClassTwo:
    def test_func_six(self, function_fixture, class_fixture, module_fixture, session_fixture):
        function_fixture["counter"] += 1
        class_fixture["counter"] += 1
        module_fixture["counter"] += 1
        session_fixture["counter"] += 1

        assert function_fixture["counter"] == 1   # Resets for each function
        assert class_fixture["counter"] == 1      # First use in this class
        assert module_fixture["counter"] == 2     # Continues from test_func_five in the module
        assert session_fixture["counter"] == 6    # Continues from previous session state

    def test_func_seven(self, function_fixture, class_fixture, module_fixture, session_fixture):
        function_fixture["counter"] += 1
        class_fixture["counter"] += 1
        module_fixture["counter"] += 1
        session_fixture["counter"] += 1

        assert function_fixture["counter"] == 1   # Resets for each function
        assert class_fixture["counter"] == 2      # Continues from test_func_six in the class
        assert module_fixture["counter"] == 3     # Continues within the module
        assert session_fixture["counter"] == 7    # Continues from previous session state

def test_func_eight(function_fixture, module_fixture, session_fixture):
    function_fixture["counter"] += 1
    module_fixture["counter"] += 1
    session_fixture["counter"] += 1

    assert function_fixture["counter"] == 1   # Resets for each function
    assert module_fixture["counter"] == 4     # Continues from previous tests in this module
    assert session_fixture["counter"] == 8    # Continues from previous session state
