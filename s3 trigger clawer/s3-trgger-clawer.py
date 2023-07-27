import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue', region_name='ap-southeast-2')  # 雪梨區域
    response = glue.start_crawler(
        Name='ga4-parquet'  # 這裡填入你的爬蟲名稱
    )
    return {
        'statusCode': 200,
        'body': response
    }
