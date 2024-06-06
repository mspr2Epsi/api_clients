pipeline {
    agent any
    
    stages {
        stage('Run Tests') {
            steps {
                sh 'python api_clients/test.py'
            }
        }
    }
}
