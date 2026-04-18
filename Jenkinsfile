pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Image') {
            steps {
                sh 'podman build --cgroup-manager=cgroupfs -t aceest-app .'
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                podman tag aceest-app docker.io/2024tm93630@wilp.bits-pilani.ac.in/aceest-app:latest
                podman push docker.io/2024tm93630@wilp.bits-pilani.ac.in/aceest-app:latest
                '''
    }
}
    }
}