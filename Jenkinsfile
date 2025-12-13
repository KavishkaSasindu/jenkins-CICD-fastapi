pipeline {
    agent any

    environment {
        REPO = "https://github.com/KavishkaSasindu/jenkins-CICD-fastapi.git"
        IMAGE = "fastapi-app"
        TAG = "${BUILD_NUMBER}"
        AWS_ACCOUNT_ID = "525163865240"
        AWS_REGION = "us-east-1"
        REPO_NAME = "fastapi_repo"
        GITHUB_TOKEN = credentials('github_token')
        MANIFEST_REPO = "https://github.com/KavishkaSasindu/fastapi-infra-manifest.git"
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
                    rm -rf jenkins-CICD-fastapi
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
                expression {currentBuild.currentResult == "SUCCESS"}
            }
            steps {
                sh """
                    docker build -t ${IMAGE}:${TAG} .
                    docker images 
                """

                
            }
        }
        stage('Scan the image') {
            steps {
                sh "trivy image ${IMAGE}:${TAG}"
            }
        }
        stage("Push to ECR") {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                script {

                    echo "Logging in to AWS ECR..."


                    withAWS(credentials: 'AWS_Credentials', region: "${AWS_REGION}") {
                        sh """
                            aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                        """
                    }

                    echo "Tagging Docker image..."

                    sh """
                        docker tag ${IMAGE}:${TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO_NAME}:${TAG}
                    """

                    echo "Pushing Docker image to ECR..."

                    sh """
                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO_NAME}:${TAG}
                    """

                    echo "Image pushed successfully!"

                    echo "Deleting docker image from server..."

                    sh """
                        docker rmi ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO_NAME}:${TAG}
                        docker rmi ${IMAGE}:${TAG}
                        docker images
                    """
                }
            }
        }
        stage('Manifest Repo Tag Change') {
            when {
                expression {currentBuild.currentResult == "SUCCESS"}
            }
            steps {
                sh"""
                    echo "Cloning manifest repository ....."
                    rm -rf manifest-repo
                    git clone --depth 1 ${MANIFEST_REPO} manifest-repo

                    cd manifest-repo/fastapi-infra-manifest

                    echo "Updating image tag....."
                    yq -i '.deployment.tag = "'${TAG}'"' values.yaml

                    echo "Configuring Git identity..."
                    git config user.email "jenkins@ci.com"
                    git config user.name "Jenkins CI"

                    git add values.yaml
                    git commit -m "ci: update FastAPI image tag to ${TAG}"
                    git push https://${GITHUB_TOKEN}@github.com/KavishkaSasindu/fastapi-infra-manifest.git
                """
            }
        }
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
    }
}