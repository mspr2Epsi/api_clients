pipeline {
    agent any

    environment {
        // Définissez DOCKER_HOST pour le pipeline
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
    }

    stages {
        stage('Preparation') {
            steps {
                script {
                    // Exécution des commandes dans un conteneur Docker Python en tant que root
                    docker.image('python:3.8-slim').inside('-u root') {
                        // Installez les dépendances dans un répertoire spécifique
                        sh 'pip install --target=/usr/local/lib/python3.8/site-packages -r requirements.txt'
                        sh 'python -m unittest discover -s test'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Tests completed successfully.'
        }
        failure {
            echo 'Tests failed. Check the logs for details.'
        }
    }
}
