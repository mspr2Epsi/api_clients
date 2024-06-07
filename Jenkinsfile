pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
       
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/mspr2Epsi/api_clients.git']]])
                

            }
        }
        stage('Verify Python Installation') {
            steps {
  
                bat 'python --version'
            }
        }
        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Check compilation') {
            steps {

                bat 'venv\\Scripts\\activate && python -m py_compile test.py'
                bat 'venv\\Scripts\\activate && python -m py_compile api_clients.py'
            }
        }
    }
}
