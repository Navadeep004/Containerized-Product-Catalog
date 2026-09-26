pipeline {

    agent {
        label 'linux'
    }

    environment {
        IMAGE_TAG = '2.0'
        DOCKER_IMAGE = 'navadeep04/product-catalog-api'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m compileall .'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t product-catalog-api:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-login',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker tag "product-catalog-api:$IMAGE_TAG" "$DOCKER_IMAGE:$IMAGE_TAG"
                        docker push "$DOCKER_IMAGE:$IMAGE_TAG"
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f k8s/namespace.yaml
                    kubectl apply -f k8s/mongodb-deployment.yaml
                    kubectl apply -f k8s/mongodb-service.yaml
                    kubectl apply -f k8s/api-deployment.yaml
                    kubectl apply -f k8s/api-service.yaml

                    kubectl rollout status deployment/product-api -n product-catalog
                '''
            }
        }  
    }

    post {

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the Jenkins console output.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}