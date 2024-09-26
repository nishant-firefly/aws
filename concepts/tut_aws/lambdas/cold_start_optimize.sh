# Enable provisioned concurrency in your Lambda function:

aws lambda put-provisioned-concurrency-config \
    --function-name MyFunction \
    --qualifier 1 \
    --provisioned-concurrent-executions 5

# This will keep 5 Lambda instances ready to handle requests without cold start delays.