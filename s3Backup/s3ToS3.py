import boto3
from datetime import datetime

"""
Lambda function to move backup files from one S3 bucket to another.

Args:
    event: The event data passed to the Lambda function.
    context: The runtime information of the Lambda function.

Returns:
    A dictionary containing the status code and body of the response.

Raises:
    Exception: If an error occurs during the backup process.
"""

def lambda_handler(event, context):
    current_date = datetime.now().strftime("%Y%m%d")
    print("Current date:", current_date)

    source_bucket = "S3_backup" # バックアップファイルが格納されているバケット
    target_bucket = "S3_other" # バックアップファイルを移動するバケット

    s3 = boto3.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=source_bucket)
        if 'Contents' in response:
            backup_files = response['Contents']
            for file in backup_files:
                key = file['Key']
                file_name = key.split('/')[-1]

                target_folder = f"{current_date}/{file_name}"

                response = s3.copy_object(
                    Bucket=target_bucket,
                    CopySource=f"{source_bucket}/{key}",
                    Key=target_folder
                )
                print("Backup file moved:", target_folder)
        else:
            print("No backup files found in the source bucket.")

        return {
            'statusCode': 200,
            'body': 'Backup process completed successfully.'
        }

    except Exception as e:
        print("An error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': 'Error occurred during backup process.'
        }
