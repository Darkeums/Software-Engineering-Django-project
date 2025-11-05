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
        stage('Build in Minikube Docker') {
            steps {
                bat '''
                REM === Switch Docker to Minikube Docker ===
                REM *** PERMANENT FIX: Overriding broken [::1] address with stable IPv4 ***
                SET DOCKER_HOST=tcp://192.168.49.2:2376
                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                '''
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