# features/environment.py

def before_scenario(context, scenario):
    """
    Set up before each scenario. Initialize shared state or global data.
    """
    print(f"Setting up scenario: {scenario.name}")
    context.browser = "Chrome"  # Example of global context for all scenarios

def after_scenario(context, scenario):
    """
    Clean up after each scenario.
    """
    print(f"Teardown after scenario: {scenario.name}")
    context.browser = None  # Clear shared state
