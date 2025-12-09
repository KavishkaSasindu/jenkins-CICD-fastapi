pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh '''
                    echo "Hello from Jenkins Pipeine"
                '''
            }
        }
        stage('Check Environment') {
            steps {
                sh '''
                    docker --version
                '''
            }
        }
        stage('check webhook') {
            steps {
                echo 'Checking webhook'
            }
        }
    }
}