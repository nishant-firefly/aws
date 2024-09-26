from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks

class MyLambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda Function that processes SQS messages
        lambda_function = lambda_.Function(self, "SQSProcessor",
                                           runtime=lambda_.Runtime.PYTHON_3_8,
                                           handler="lambda_function.lambda_handler",
                                           code=lambda_.Code.from_asset("lambda_code"))

        # SQS Queue
        queue = sqs.Queue(self, "MyQueue")

        # Grant the Lambda function permission to read from the SQS queue
        queue.grant_consume_messages(lambda_function)

        # Add SQS event source to Lambda
        lambda_function.add_event_source(lambda_.event_sources.SqsEventSource(queue))

        # SNS Topic
        topic = sns.Topic(self, "MyTopic")
        
        # Subscribe Lambda to SNS topic
        topic.add_subscription(subs.LambdaSubscription(lambda_function))

        # Step Function Definition (Simple pass state)
        definition = sfn.Pass(self, "HelloWorld")

        # Step Function State Machine
        state_machine = sfn.StateMachine(self, "MyStateMachine",
                                         definition=definition)

        # Lambda Function that invokes Step Functions
        lambda_step_function_invoker = lambda_.Function(self, "StepFunctionInvoker",
                                                        runtime=lambda_.Runtime.PYTHON_3_8,
                                                        handler="lambda_function.lambda_handler",
                                                        code=lambda_.Code.from_asset("lambda_code"))

        # Grant the Lambda function permission to invoke the Step Function
        state_machine.grant_start_execution(lambda_step_function_invoker)

"""
SQS: A queue is created, and a Lambda function is triggered whenever a message is sent to the queue.
SNS: An SNS topic is created, and the same Lambda function is subscribed to the topic.
Step Functions: Another Lambda function invokes a simple Step Function (HelloWorld).
"""