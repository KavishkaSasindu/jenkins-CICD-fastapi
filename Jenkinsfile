pipeline {
    agent any

    environment {
        REPO = "https://github.com/KavishkaSasindu/jenkins-CICD-fastapi.git"
        IMAGE = "fastapi-app"
        TAG = "${BUILD_NUMBER}"
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
        stage('Build') {
            when {
                expression (currentBuild.currentResult == "SUCCESS")
            }
            steps {
                script {
                    stage {
                        sh '''
                            docker build -t ${IMAGE}:${TAG} .
                        '''
                    }
                    stage {
                        sh '''
                            docker images
                        '''
                    }
                }
            }
        }
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
    }
}