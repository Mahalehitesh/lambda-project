def lambda_handler(event, context):
    
    # Debug print (you can see this in CloudWatch logs)
    print("Lambda function triggered successfully")

    # Sample response
    return {
        'statusCode': 200,
        'body': 'Hello! Lambda updated from GitHub CI/CD'
    }
