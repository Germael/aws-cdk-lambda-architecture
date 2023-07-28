from aws_cdk import (
    Stack,
    aws_events,
    aws_events_targets,
    aws_lambda,
    Duration
)
from constructs import Construct


class AwsLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        custom_layer = aws_lambda.LayerVersion(self,
                                            'lambda_layer',
                                            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_8],
                                            code=aws_lambda.Code.from_asset('layer/'),
                                            description='layer for custom lambda')

        custom_lambda = aws_lambda.Function(
            self,
            id='custom_lambda',
            handler='handler.lambda_handler',
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_asset('functions/custom_lambda'),
            timeout=Duration.seconds(15),
            layers=[custom_layer]
        )
        rule = aws_events.Rule(self,
                               'lambda_func_cron_rule',
                               schedule=aws_events.Schedule.cron(minute='0', hour='1', day='*/2'))

        rule.add_target(aws_events_targets.LambdaFunction(custom_lambda))
