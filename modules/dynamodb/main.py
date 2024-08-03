import pulumi
import pulumi_aws as aws

config = pulumi.Config()
table_name = config.require("dynamodb_table_name")
billing_mode = config.require("dynamodb_billing_mode")
hash_key = config.require("dynamodb_hash_key")


def dynamodb_table():
    aws.dynamodb.Table(
        "dynamodb_table",
        name=table_name,
        billing_mode=billing_mode,
        hash_key=hash_key,
        deletion_protection_enabled=False,

        attributes=[{
            "name": hash_key,
            "type": "S"
        }]
    )
