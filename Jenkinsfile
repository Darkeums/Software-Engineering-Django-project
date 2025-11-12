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
                REM === 1. Switch Docker to Minikube Docker (Sets certs/TLS/etc.) ===
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat
                
                REM === 2. OVERRIDE DOCKER_HOST to use IPv4 instead of IPv6 ([::1]) ===
                REM Get the IPv4 address of the Minikube host (e.g., 192.168.49.2)
                FOR /F "tokens=*" %%i IN ('minikube ip') DO SET MINIKUBE_IP=%%i
                
                REM Extract the dynamic port number assigned by minikube docker-env (e.g., 61967)
                FOR /F "tokens=3 delims=:" %%p IN ('echo %DOCKER_HOST%') DO SET DOCKER_PORT=%%p

                SET DOCKER_HOST=tcp://%MINIKUBE_IP%:%DOCKER_PORT%
                
                ECHO DOCKER_HOST successfully overridden to: %DOCKER_HOST%

                REM === 3. Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                '''
            }
        }
        stage('Deploy to Minikube') {
            steps {
                bat '''
                REM === Apply the updated deployment manifest ===
                kubectl apply -f deployment.yaml
                REM === Apply the service manifest (THE CRITICAL FIX WE MADE) ===
                kubectl apply -f service.yaml 
                REM === Ensure the rollout completes ===
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}
