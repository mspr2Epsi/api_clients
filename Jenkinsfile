pipeline {
    agent any

    // Commentez ou retirez cette section si aucune variable d'environnement n'est nécessaire
    // environment {
    //     SOME_ENV_VAR = 'value'
    // }

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                sudo apt update
                sudo apt install python3 python3-pip -y
                '''
            }
        }
        stage('Preparation') {
            steps {
                echo 'Installation des dépendances...'
                sh 'pip install -r requirements.txt' // Assurez-vous que vous avez un fichier requirements.txt
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Exécution des tests...'
                sh 'python -m unittest discover -s tests' // Assurez-vous que le dossier 'tests' contient vos tests
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
