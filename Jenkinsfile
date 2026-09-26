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
                sh 'docker build -t product-catalog-api:1.0 .'
            }
        }    
    }
}