# Flask API Project Template

This project is a template for creating Flask applications configured to work with HTTPS using Docker, Miniconda, and DigitalOcean Secrets Manager.

## Repository Structure

```
myproject/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── api/
│ │ │ ├── init.py
│ │ │ ├── routes.py
│ ├── config.py
│ ├── run.py
│ ├── tests/
│ │ ├── test_routes.py
├── docker/
│ ├── development/
│ │ ├── Dockerfile
│ │ ├── docker-compose.yml
│ │ ├── nginx/
│ │ │ ├── nginx.conf
│ │ │ ├── certs/
│ │ │ │ ├── server.crt
│ │ │ │ ├── server.key
│ ├── production/
│ │ ├── Dockerfile
│ │ ├── docker-compose.yml
│ │ ├── .env
│ │ ├── get_secrets.py
│ │ ├── nginx/
│ │ │ ├── nginx.conf
│ │ │ ├── certs/
├── environment-dev.yml
├── environment-prod.yml
├── .gitignore
└── README.md
```


## Requirements

- Docker
- Docker Compose

## Development Environment Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/richardesp/flask-conda-rest-template
cd flask-conda-rest-template
```

### Step 2: Create the Development Environment

Navigate to the development directory and bring up the services with Docker Compose.

```bash
cd docker/development
docker-compose up --build
```

### Step 3: Real-Time Code Changes

Changes in the code within the backend/ directory will automatically reflect due to volume mounting.

### Step 4: Execute Commands Inside the Container

To execute commands inside the web container:

```bash
docker-compose exec web /bin/sh
```

### Step 5: Run Tests

To run the tests:

```bash
docker-compose exec web pytest
```

### Step 6: Update Dependencies

Add new dependencies in the environment-dev.yml file.
Rebuild the image to install the new dependencies.

```bash
docker-compose build web
docker-compose up -d
```

## Production Environment Setup

### Step 1: Configure Secrets in DigitalOcean

Store your certificates (server.crt and server.key) in DigitalOcean Secrets Manager.

### Step 2: Create the .env File

Create the .env file in docker/production/ and add your environment variables (you have an example to fill in directly).

### Step 3: Create the Production Environment

Navigate to the production directory and bring up the services with Docker Compose.

```bash
cd docker/production
docker-compose up --build
```

### Step 4: Execute Commands Inside the Container

To execute commands inside the web container:

```bash
docker-compose exec web /bin/sh
```

### Step 5: Update Dependencies

Add new dependencies in the environment-prod.yml file.
Rebuild the image to install the new dependencies.

```bash
docker-compose build web
docker-compose up -d
```

## Using Nginx

Nginx is used to handle HTTPS traffic. The configuration can be found in:

- docker/development/nginx/nginx.conf
- docker/production/nginx/nginx.conf

## SSL Certificates

The certificates for the development environment should be located at:

```bash
docker/development/nginx/certs/server.crt
docker/development/nginx/certs/server.key
```

For production, they are retrieved from DigitalOcean Secrets Manager.

## Best Practices

- Do not upload certificates or sensitive files to the repository. Ensure that .env files and certificates are listed in .gitignore.
- Keep dependencies up to date. Update the environment-dev.yml and environment-prod.yml files when adding new dependencies and rebuild the images.
- Use a virtual environment. In local development environments, consider using a virtual environment (venv) to manage dependencies.

## Additional Recommendations

- Documentation: Maintain comprehensive documentation for your project, including setup instructions, API documentation, and examples of usage. This helps new developers understand and contribute to the project quickly.
- CI/CD Integration: Implement Continuous Integration and Continuous Deployment (CI/CD) pipelines to automate testing, building, and deployment processes. This ensures code quality and streamlines deployment.
- Code Quality: Use linters and formatters to maintain code quality and consistency. Tools like flake8, black, and pylint can be integrated into your development workflow.
- Security: Regularly review and update your dependencies to mitigate security vulnerabilities. Use tools like Dependabot to automate this process.
- Monitoring and Logging: Implement monitoring and logging to track the performance and errors in your application. Tools like Prometheus, Grafana, and ELK stack (Elasticsearch, Logstash, Kibana) can be useful.
- Scalability: Design your application with scalability in mind. Use Docker Swarm or Kubernetes for orchestration and consider using cloud services to handle scaling.

## Contact

For any questions or support, contact me via GitHub (richardesp).

