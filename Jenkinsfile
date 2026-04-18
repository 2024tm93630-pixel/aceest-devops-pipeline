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
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | podman login docker.io -u "$DOCKER_USER" --password-stdin
                    podman tag aceest-app docker.io/$DOCKER_USER/aceest-app:latest
                    podman push docker.io/$DOCKER_USER/aceest-app:latest
                    '''
                }
            }
        }
    }
}