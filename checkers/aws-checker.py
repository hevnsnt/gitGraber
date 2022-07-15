from awscliv2.api import AWSAPI
from awscliv2.exceptions import AWSCLIError

aws_api = AWSAPI()
aws_api.set_credentials("profile_name", "AKIAIRKJSB6E2QHII7WQ", "GsHQzLsIsukXQAagNcVU+w2/jVDVEI9Bcw9tAyEo", "", "ap-northeast-1")
#aws_api.assume_role("name", "source_profile", "role_arn")

try:
    output = aws_api.execute(["s3", "ls"])
except AWSCLIError as e:
    print(f"Something went wrong: {e}")
else:
    print(output)