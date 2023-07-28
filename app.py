#!/usr/bin/env python3
import aws_cdk as cdk

from cdk.main_stack import AwsLambdaStack


app = cdk.App()
AwsLambdaStack(app, "AwsLambdaStack", env={
    'region': 'us-east-1'
})

app.synth()
