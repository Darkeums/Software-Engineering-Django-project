pipeline {
    agent any
    triggers {
        // Poll GitHub every 2 minutes
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Darkeums/Software-Engineering-Django-project.git'
            }
        }
        stage('Set Docker Environment') {
            steps {
                bat '''
                REM *** Use minikube to set the correct Docker environment variables ***
                FOR /f "tokens=*" %%i IN ('minikube -p minikube docker-env --shell cmd') DO %%i
                '''
                // NOTE: This dynamically sets DOCKER_HOST, DOCKER_TLS_VERIFY, and DOCKER_CERT_PATH
            }
        }
        stage('Build in Minikube Docker') {
            steps {
                bat '''
                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                '''
                // The environment variables are now set by the previous stage.
            }
        }
        stage('Deploy to Minikube') {
            steps {
                bat '''
                REM === Apply the updated deployment manifest ===
                kubectl apply -f deployment.yaml
                REM === Ensure the rollout completes ===
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}