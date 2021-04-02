import boto3

TABLE_NAME = "electionResults"


class DB:
    @property
    def client(self):
        return boto3.client("dynamodb", region_name="eu-central-1")
