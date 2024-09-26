#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_app_python.cdk_stack import CdkAppStack

app = cdk.App()
CdkAppStack(app, "CdkAppStack")
app.synth()
