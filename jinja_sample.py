from jinja2 import Environment, BaseLoader, DebugUndefined
import json

# Define the custom function to build the card reference ID
def build_card_reference_id(accountId, sorId, tokenizedOriginatingPlastic):
    return f"{accountId},{sorId},{tokenizedOriginatingPlastic}"

# Custom filters for Jinja2
CUSTOM_TEMPLATE_FILTERS = {
    "build_card_reference_id": build_card_reference_id
}

# Template engine setup
class TemplateEngine:
    def __init__(self):
        self.env = Environment(loader=BaseLoader(), undefined=DebugUndefined)
        # Add custom filters to the environment
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

# Example template with cardReferenceId inside transaction decisions
template = """
{
    "url": "{{host}}/private/18172/transaction-financial-adjustment",
    "method": "POST",
    "headers": {
        "Accept": "application/json;v=3",
        "Content-Type": "application/json",
        "Client-Correlation-Id": "claims-fulfillment-actions-api:{{ClientCorrelationId}}",
        "Client-Id": "claims-fulfillment-actions-api",
        "User-Id": "claims-fulfillment-actions-api"
    },
    "payload": {
        "accountId": "{{accountId}}",
        "sorId": "{{sorId}}",
        "claimId": "{{claimId}}",
        "caseNumber": "{{caseNumber}}",
        "caseType": "{{caseType}}",
        "caseSubType": "{{caseSubtype}}",
        "chargeOffDate": "{{chargeOffDate}}",
        "transactionDecisions": [
            {
                "transaction": {
                    "claimTransactionId": "{{claimTransactionId}}",
                    "memoPostedIndicator": "{{memoPostedIndicator}}",
                    "transactionDate": "{{transactionDate}}",
                    "statementDate": "{{statementDate}}",
                    "postedSequenceNumber": "{{postedSequenceNumber}}",
                    "transactionState": "{{transactionState}}",
                    "transactionPostedDate": "{{transactionPostedDate}}",
                    "transactionAmount": "{{transactionAmount}}",
                    "disputeAmount": "{{disputeAmount}}",
                    "acquirerReferenceNumber": "{{acquirerReferenceNumber}}",
                    "merchantName": "{{merchantName}}",
                    "originalCurrencyCode": "{{originalCurrencyCode}}",
                    "transactionLifecycleId": "{{transactionLifecycleId}}",
                    "transactionCode": "{{transactionCode}}",
                    "undecisionedAmount": "{{undecisionedAmount}}",
                    "transactionCategoryCode": "{{transactionCategoryCode}}",
                    "tokenizedOriginatingPlastic": "{{tokenizedOriginatingPlastic}}",
                    "recurringIndicator": "{{recurringIndicator}}",
                    "transactionInsertionDate": "{{transactionInsertionDate}}"
                },
                "cardReferenceId": "{{ accountId | build_card_reference_id(sorId, tokenizedOriginatingPlastic) }}",
                "decisions": [
                    {
                        "decisionReferenceId": "{{decisionReferenceId}}",
                        "previousDecisionId": "{{previousDecisionId}}",
                        "amount": "{{amount}}",
                        "liableParty": "{{liableParty}}",
                        "resolutionStatus": "{{resolutionStatus}}",
                        "chargebackReasonCode": "{{chargebackReasonCode}}",
                        "decisionSubStatus": "{{decisionSubStatus}}"
                    }
                ]
            }
        ]
    },
    "response": {
        "systematicFinancialsSupported": true
    }
}
"""

# Parameters that will be passed to the template
params = {
    "host": "https://your-url",
    "ClientCorrelationId": "correlation123",
    "accountId": "10000878972",
    "sorId": "7",
    "claimId": "123",
    "caseNumber": "191009221202478",
    "caseType": "FRAUD",
    "caseSubtype": "TRANSACTION",
    "chargeOffDate": "2019-08-16",
    "claimTransactionId": "1178397",
    "memoPostedIndicator": False,
    "transactionDate": "2019-08-16T04:00:00.000Z",
    "statementDate": "2019-08-04T04:00:00.000Z",
    "postedSequenceNumber": "2001333",
    "transactionState": "POSTED",
    "transactionPostedDate": "2019-08-16T04:00:00.000Z",
    "transactionAmount": 149.99,
    "disputeAmount": 149.99,
    "acquirerReferenceNumber": "252910792280000023502",
    "merchantName": "Tony's Pizza and Games",
    "originalCurrencyCode": "USD",
    "transactionLifecycleId": "MCW742766",
    "transactionCode": "1001",
    "undecisionedAmount": 0.0,
    "transactionCategoryCode": "0001",
    "tokenizedOriginatingPlastic": "4234testing1234",
    "recurringIndicator": False,
    "transactionInsertionDate": "2019-11-14T00:00:00.000Z",
    "decisionReferenceId": "decision123",
    "previousDecisionId": "prevDecision123",
    "amount": 149.99,
    "liableParty": "CUSTOMER",
    "resolutionStatus": "RESOLVED_CUSTOMER_RESPONSIBLE",
    "chargebackReasonCode": "1234",
    "decisionSubStatus": "RESOLVED_CUSTOMER_RESPONSIBLE_ACCEPTED"
}

# Generate the final filled template
filled_template = create_template_request(template, params)

# Print the generated JSON
print(json.dumps(filled_template, indent=4))
