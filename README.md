# Python Home Automation Microservices

This project implements a home automation system using Python microservices. It was developed as an alternative to Raspberry Pi-based solutions due to connectivity limitations at the university.

The system consists of multiple independent microservices, each responsible for a specific sensor or device, such as temperature, humidity, light, fan, buzzer, motion detection, and more. These microservices communicate over HTTP and can be deployed on cloud platforms such as AWS using containerization technologies.

## Project Repository

The full Python code and microservices implementations are available here:  
[https://github.com/njomzabehadini23/microservicesPython](https://github.com/njomzabehadini23/microservicesPython)

## Architecture Overview

- Each device or sensor functionality runs as an individual Flask-based microservice.
- Services are containerized using Docker.
- Communication is managed through a gateway service.
- Deployment is designed to run on AWS ECS with Fargate for serverless container hosting.
- AWS Elastic Container Registry (ECR) stores container images.
- Task definitions and service deployments are configured for automatic scaling and reliability.

## Deployment

The application is deployed to AWS Elastic Container Service (ECS) using:

- Docker to build container images.
- AWS CLI and Elastic Beanstalk CLI tools for deployment and management.
- AWS ECR to store Docker images.
- AWS ECS Fargate to run containers without managing servers.

## How to Use

1. Clone the repository:  
   `git clone https://github.com/njomzabehadini23/microservicesPython.git`

2. Build Docker images for each service.

3. Push images to your AWS ECR repositories.

4. Register task definitions and deploy services on AWS ECS.

5. Access the gateway service endpoint to interact with the home automation system.

## Notes

- The project was developed for academic purposes to simulate a home automation system in a restricted network environment.
- It is designed for extensibility; additional sensors or devices can be added as independent services.
- Ensure you have valid AWS credentials and permissions to deploy and manage ECS resources.

## Contact

For questions or collaboration, please open an issue or contact me through GitHub.

---

*Project by njomzabehadini23*
