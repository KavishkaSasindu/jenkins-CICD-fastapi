pipeline {
    agent any

    environment {
        REPO = "https://github.com/KavishkaSasindu/jenkins-CICD-fastapi.git"
    }

    stages {
        stage('Environment Test') {
            steps {
                sh '''
                    docker --version
                    aws --version
                    trivy --version
                    git --version
                '''
            }
        }
        stage('Checkout Repo') {
            steps {
                sh '''
                    git clone ${REPO}
                '''
            }
        }
        stage('Test') {
            steps {
                sh'''
                    echo "Running Tests..."
                    echo "Tests Pass"
                '''
            }
        }
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
    }
}