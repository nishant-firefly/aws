#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkAppStack } from '../lib/cdk_app_stack';

const app = new cdk.App();
new CdkAppStack(app, 'CdkAppStack');
