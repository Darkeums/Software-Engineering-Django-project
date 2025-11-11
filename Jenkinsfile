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
                REM === Switch Docker to Minikube Docker using the .bat file method ===
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat
                REM === Build Django image inside Minikube Docker, using the root path (.) ===
                docker build -t mydjangoapp:latest .
                '''
            }
        }
        stage('Deploy to Minikube') {
            steps {
                bat '''
                REM === Apply the updated deployment manifest (now in root) ===
                kubectl apply -f deployment.yaml
                REM === Apply the service manifest (THE CRITICAL FIX) ===
                kubectl apply -f service.yaml 
                REM === Ensure the rollout completes ===
                kubectl rollout status deployment/django-deployment
                '''
            }
        }
    }
}
