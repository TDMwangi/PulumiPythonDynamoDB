# Pulumi Python DynamoDB

Pulumi allows for infrastructure as code (IaC) using familiar programming languages.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [Python](https://www.python.org/downloads/) (version 3.7 or higher)
- [AWS CLI](https://aws.amazon.com/cli/) (configured with the correct credentials)

## Setting Up the Pulumi Project

1. **Clone the Repository**

   First, clone this repository to your local machine:

   ```sh
   git clone https://github.com/TDMwangi/PulumiPythonDynamoDB.git
   cd PulumiPythonDynamoDB
   ```

3. **Activate Virtual Environment**

  Create and activate the virtual environment:

  ```sh
  python -m venv venv
  source venv/bin/activate
  ```

2. **Install Dependencies**

   Install the required Python dependencies by running:

   ```sh
   pip install -r requirements.txt
   ```

## Working with Pulumi Stacks

Pulumi uses the concept of "stacks" to represent different environments (e.g., `dev`, `staging`, `prod`). Each stack is an isolated instance of your infrastructure that can have its own configuration.

### 1. Creating a New Stack

To create a new stack, use the `pulumi stack init` command followed by the stack name:

```sh
# Create a development stack
pulumi stack init dev

# Create a staging stack
pulumi stack init staging

# Create a production stack
pulumi stack init prod
```

### 2. Listing Existing Stacks

You can list all the stacks associated with your project using:

```sh
pulumi stack ls
```

This command will display the available stacks and indicate which stack is currently selected.

### 3. Selecting the Correct Stack

To work with a specific stack, select it using the `pulumi stack select` command:

```sh
# Select the dev stack
pulumi stack select dev

# Select the staging stack
pulumi stack select staging

# Select the prod stack
pulumi stack select prod
```

### 4. Configuring Stack-Specific Settings

Each stack can have its own configuration settings stored in `Pulumi.<stack-name>.yaml` files. You can set configuration values using the Pulumi CLI:

```sh
# Set configuration for the dev stack
pulumi config set aws:region us-west-2 --stack dev
pulumi config set dynamodb_table_name dev_table --stack dev

# Set configuration for the staging stack
pulumi config set aws:region us-east-1 --stack staging
pulumi config set dynamodb_table_name staging_table --stack staging

# Set configuration for the prod stack
pulumi config set aws:region us-east-1 --stack prod
pulumi config set dynamodb_table_name prod_table --stack prod
```

Alternatively, you can manually edit the `Pulumi.<stack-name>.yaml` files in your project directory:

**Example `Pulumi.dev.yaml`:**
```yaml
config:
  aws:region: us-west-2
  dynamodb_table_name: dev_table
  dynamodb_billing_mode: PAY_PER_REQUEST
  dynamodb_hash_key: dev_app_id
```

**Example `Pulumi.staging.yaml`:**
```yaml
config:
  aws:region: us-east-1
  dynamodb_table_name: staging_table
  dynamodb_billing_mode: PAY_PER_REQUEST
  dynamodb_hash_key: staging_app_id
```

**Example `Pulumi.prod.yaml`:**
```yaml
config:
  aws:region: us-east-1
  dynamodb_table_name: prod_table
  dynamodb_billing_mode: PROVISIONED
  dynamodb_hash_key: prod_app_id
```

### 5. Running a Pulumi Deployment

After selecting the correct stack and configuring the necessary settings, you can deploy your infrastructure with:

```bash
pulumi up
```

Pulumi will prompt you to confirm the changes it plans to make. Review the proposed changes and confirm to proceed with the deployment.

## Cleaning Up Resources

To destroy the resources associated with a specific stack, use:

```bash
pulumi destroy --stack <stack-name>
```

This command will delete all resources managed by Pulumi for that stack.
