import boto3
import json

def lambda_handler(event, context):
    glue = boto3.client('glue')

    crawler_name = 'ga4-csv'
    job_name = 'visual ga4 transform'
    
    # Get the state of the crawler from the event
    state = event['detail']['state']
    if state == 'SUCCEEDED':
        # If the crawler has succeeded, start the job
        response = glue.start_job_run(JobName=job_name)
        print(f'Started job run {response["JobRunId"]}')
    else:
        print(f'Crawler {crawler_name} is in state {state}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
