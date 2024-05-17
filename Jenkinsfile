pipeline {
    agent any

    tools {
        // S'assure que Docker est disponible pour Jenkins
        docker '19.03' // Assurez-vous que cette version correspond à celle disponible sur votre serveur Jenkins
    }

    stages {
        stage('Preparation') {
            steps {
                // Utilisation de l'image Docker Python pour installer les dépendances et exécuter les tests
                script {
                    docker.image('python:3.8-slim').inside {
                        sh 'pip install -r requirements.txt'
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
