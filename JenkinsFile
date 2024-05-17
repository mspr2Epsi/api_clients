pipeline {
    agent any

    environment {
        // Définir les variables d'environnement requises
    }

    stages {
        stage('Preparation') {
            steps {
                echo 'Installation des dépendances...'
                sh 'pip install -r requirements.txt' // Assurez-vous que vous avez un fichier requirements.txt
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Exécution des tests...'
                sh 'python -m unittest test.py' // Exécute le script de test
            }
        }
    }

    post {
        success {
            echo 'Les tests ont réussi sans erreurs.'
        }
        failure {
            echo 'Les tests ont échoué. Vérifiez les logs pour plus de détails.'
        }
    }
}
