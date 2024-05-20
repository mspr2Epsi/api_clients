pipeline {
    agent any

    environment {
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        RABBITMQ_HOST = 'rabbitmq'
        RABBITMQ_PORT = '5672'
        DB_HOST = 'db'  // Utilisé pour se connecter depuis les autres conteneurs
        DB_PORT = '3306'
    }

    stages {
        stage('Démarrer la base de données') {
            steps {
                script {
                    // Utilisation de mysql:8.0, changez selon vos besoins
                    sh """
                    docker run -d \
                    --network jenkins-network \
                    --name db \
                    -e MYSQL_ROOT_PASSWORD=password \
                    -e MYSQL_DATABASE=mspr2 \
                    -v \$(pwd)/clients.sql:/docker-entrypoint-initdb.d/init.sql:ro \
                    mysql:8.0
                    """
                }
            }
        }
        stage('Preparation') {
            steps {
                script {
                    docker.image('python:3.12.3-slim').inside('-u root --network=jenkins-network') {
                        sh 'pip install --target=/usr/local/lib/python3.12/site-packages -r requirements.txt'
                        sh 'python3 --version'
                        sh 'python -m unittest discover -s test'
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker stop db rabbitmq jenkins'
            sh 'docker rm db rabbitmq jenkins'
        }
        success {
            echo 'Tests completed successfully.'
        }
        failure {
            echo 'Tests failed. Check the logs for details.'
        }
    }
}
