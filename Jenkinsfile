pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
    DOCKERHUB_USER = 'devpraveens'
    KUBECONFIG_CREDENTIAL = 'kubeconfig'
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build and Push Images') {
      parallel {
        stage('Backend') {
          steps {
            dir('backend') {
              script {
                docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                  def img = docker.build("${DOCKERHUB_USER}/3tier-backend:${env.BUILD_NUMBER}")
                  img.push()
                  img.push('latest')
                }
              }
            }
          }
        }
        stage('Frontend') {
          steps {
            dir('frontend') {
              script {
                docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                  def img = docker.build("${DOCKERHUB_USER}/3tier-frontend:${env.BUILD_NUMBER}")
                  img.push()
                  img.push('latest')
                }
              }
            }
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([file(credentialsId: KUBECONFIG_CREDENTIAL, variable: 'KUBE_CONFIG')]) {
          sh 'mkdir -p $HOME/.kube && cp $KUBE_CONFIG $HOME/.kube/config'
          sh 'kubectl apply -f infra/namespace.yaml'
          sh 'kubectl apply -R -f infra/'
        }
      }
    }
  }
}
