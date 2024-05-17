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
                    // Exécution des commandes dans un conteneur Docker Python
                    docker.image('python:3.8-slim').inside {
                        // Installez les dépendances et exécutez les tests ici
                        sh 'pip install --user -r requirements.txt'
                        sh 'python -m unittest discover -s tests'
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
