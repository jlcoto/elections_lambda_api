import boto3

TABLE_NAME = "electionResults"


class DB:
    @property
    def session(self):
        return boto3.Session(profile_name="jose_default")

    @property
    def client(self):
        return self.session.client("dynamodb", region_name="eu-central-1")
