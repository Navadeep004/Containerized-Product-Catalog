pipeline {

    agent {
        label 'linux'
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
                sh 'docker build -t product-catalog-api:2.0 .'
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
                        docker tag product-catalog-api:2.0 "$DOCKER_USERNAME/product-catalog-api:2.0"
                        docker push "$DOCKER_USERNAME/product-catalog-api:2.0"
                        docker logout
                    '''
                }
            }
        }  
    }
}