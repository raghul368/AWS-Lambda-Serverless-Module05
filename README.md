# Module 05 – AWS Lambda & Serverless

Learning project for the AWS Cloud & DevOps internship at Codomax Digital Solutions.

## Repository files
- `lambda/lambda_function.py` — sample Python AWS Lambda handler.
- `website/index.html` — responsive project overview website.

## Deploy the sample Lambda
1. Open AWS Lambda in the AWS Console.
2. Create a function using a Python runtime.
3. Copy `lambda/lambda_function.py` into the function code editor.
4. Deploy and test the function.
5. Create an HTTP API in Amazon API Gateway.
6. Add a Lambda integration and a `GET /hello` route.
7. Deploy the API and test its invoke URL.

## View the website
Open `website/index.html` in a browser, or host it using a static website hosting service.

## Important
This repository contains sample code and documentation; it does not provision AWS resources automatically. Use least-privilege IAM permissions, never commit AWS credentials or secrets, and review AWS pricing before deployment.
