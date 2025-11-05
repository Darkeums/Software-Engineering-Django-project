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
                REM *** FINAL FIX: Overriding with stable IP and required TLS security variables ***
                SET DOCKER_HOST=tcp://192.168.49.2:2376
                SET DOCKER_TLS_VERIFY=1
                SET DOCKER_CERT_PATH=C:\\Users\\janaj\\.minikube\\certs
                
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