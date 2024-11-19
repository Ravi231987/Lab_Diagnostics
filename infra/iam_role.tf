provider "aws" {
  region = "us-east-1"  # Change to your preferred region
}


# IAM role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "lambda_etl_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# IAM policy attachment for Lambda to allow S3 access and logging
resource "aws_iam_policy_attachment" "lambda_s3_policy" {
  name       = "lambda-s3-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  roles      = [aws_iam_role.lambda_role.name]
}

resource "aws_iam_policy_attachment" "lambda_logs_policy" {
  name       = "lambda-logs-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
  roles      = [aws_iam_role.lambda_role.name]
}

# IAM role for AWS Glue job
resource "aws_iam_role" "glue_role" {
  name = "glue_etl_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
      }
    ]
  })
}

# IAM policy attachment for Glue to allow S3 access
resource "aws_iam_policy_attachment" "glue_s3_policy" {
  name       = "glue-s3-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  roles      = [aws_iam_role.glue_role.name]
}

# IAM policy attachment for Glue to allow logging
resource "aws_iam_policy_attachment" "glue_logs_policy" {
  name       = "glue-logs-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
  roles      = [aws_iam_role.glue_role.name]
}
