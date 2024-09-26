from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    core
)

class CdkAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table Definition
        table = dynamodb.Table(self, "API_Template_Table",
                               partition_key=dynamodb.Attribute(name="PK", type=dynamodb.AttributeType.STRING),
                               sort_key=dynamodb.Attribute(name="SK", type=dynamodb.AttributeType.STRING))

        # Lambda Function Definition
        api_call_lambda = _lambda.Function(self, "GenericApiCallLambda",
                                           runtime=_lambda.Runtime.PYTHON_3_8,
                                           handler="lambda_function.lambda_handler",
                                           code=_lambda.Code.from_asset("lambda_code"),
                                           environment={
                                               "API_BASE_URL": "https://api.example.com"
                                           })

        # Grant Lambda permission to read/write to DynamoDB
        table.grant_read_write_data(api_call_lambda)

        # Step Function to fetch template from DynamoDB and call Lambda
        fetch_template_task = tasks.DynamoGetItem(self, "FetchTemplateFromDynamoDB", 
                                                  table=table,
                                                  key={
                                                      "PK": tasks.DynamoAttributeValue.from_string(sfn.JsonPath.string_at("$.templateName")),
                                                      "SK": tasks.DynamoAttributeValue.from_string(sfn.JsonPath.string_at("$.method"))
                                                  })
        
        lambda_invoke_task = tasks.LambdaInvoke(self, "InvokeLambdaToCallAPI", 
                                                lambda_function=api_call_lambda,
                                                payload=sfn.TaskInput.from_object({
                                                    "template": sfn.JsonPath.object_at("$.template.Item"),
                                                    "params": sfn.JsonPath.object_at("$.params")
                                                }),
                                                result_path="$.apiResponse")
        
        definition = fetch_template_task.next(lambda_invoke_task).next(sfn.Pass(self, "Success"))

        sfn.StateMachine(self, "MyStateMachine", definition=definition)
