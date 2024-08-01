from modules.dynamodb.main import dynamodb_table

service_init = [
    dynamodb_table
]


if __name__ == "__main__":
    for service in service_init:
        service()
