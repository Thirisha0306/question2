pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',url: 'https://github.com/Thirisha0306/question2.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python calculator.py 20 + 10'
                bat 'python calculator.py 20 - 10'
                bat 'python calculator.py 20 "*" 10'
                bat 'python calculator.py 20 / 10'
            }
        }
    }
}