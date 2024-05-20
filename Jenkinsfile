pipeline {
    agent any

    environment {
        // Définissez DOCKER_HOST pour le pipeline
        DOCKER_HOST = 'tcp://host.docker.internal:2375'
        RABBITMQ_HOST = 'rabbitmq'  // Nom du service RabbitMQ
        RABBITMQ_PORT = '5672'      // Port par défaut de RabbitMQ
    }

    stages {
        stage('Lancer la Base de Données') {
            steps {
                script {
                    // Créer et démarrer le conteneur de base de données
                    sh 'docker run -d --name db_container -e MYSQL_ROOT_PASSWORD=password --network jenkins-network mysql:5.7'
                }
            }
        }
        stage('Preparation') {
            steps {
                script {
                    // Exécution des commandes dans un conteneur Docker Python en tant que root
                    docker.image('python:3.12.3-slim').inside('-u root --network=jenkins-network') {
                        // Installez les dépendances dans un répertoire spécifique
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
            // Arrêter et nettoyer les conteneurs de base de données et autres services
            sh 'docker rm -f db_container'
            sh 'docker-compose -f docker-compose.yml down'
        }
        success {
            echo 'Tests completed successfully.'
        }
        failure {
            echo 'Tests failed. Check the logs for details.'
        }
    }
}