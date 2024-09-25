# features/environment.py

def before_scenario(context, scenario):
    """
    This hook runs before every scenario.
    It's used here to initialize shared context or global state.
    """
    print(f"\n[Setup] Starting scenario: {scenario.name}")
    context.browser = "Chrome"  # Simulated browser (for demo purposes)
    context.logged_in = False

def after_scenario(context, scenario):
    """
    This hook runs after every scenario.
    It's used here to clean up any resources initialized during the test.
    """
    print(f"[Teardown] Finished scenario: {scenario.name}")
    context.browser = None  # Clean up the browser
    context.logged_in = False
