from jinja2 import Environment, BaseLoader, DebugUndefined
import json

# Define the custom function to build the card reference ID
def build_card_reference_id(accountId, sorId, tokenizedOriginatingPlastic):
    return f"{accountId},{sorId},{tokenizedOriginatingPlastic}"

# Custom filters for Jinja
CUSTOM_TEMPLATE_FILTERS = {
    "build_card_reference_id": build_card_reference_id
}

# Template engine setup
class TemplateEngine:
    def __init__(self):
        self.env = Environment(loader=BaseLoader(), undefined=DebugUndefined)
        self.env.filters.update(CUSTOM_TEMPLATE_FILTERS)
    
    def fill(self, template: str, params: dict):
        # Parse the template and replace with the params
        template_obj = self.env.from_string(template)
        return template_obj.render(params)

# Function to create the template request
def create_template_request(template: str, params: dict) -> dict:
    template_engine = TemplateEngine()
    
    if len(params) == 0:
        raise ValueError("Params is empty!")
    
    # Fill the template with params
    filled_event = template_engine.fill(template, params)
    
    return json.loads(filled_event)

# Example usage
template = """
{
    "accountId": "{{ accountId }}",
    "sorId": "{{ sorId }}",
    "cardReferenceId": "{{ accountId | build_card_reference_id(sorId, tokenizedOriginatingPlastic) }}",
    "transaction": {
        "claimTransactionId": "{{ claimTransactionId }}"
    }
}
"""

params = {
    "accountId": "10000878972",
    "sorId": "7",
    "tokenizedOriginatingPlastic": "4234testing1234",
    "claimTransactionId": "1178397"
}

# Generate the final filled template
filled_template = create_template_request(template, params)
print(filled_template)
