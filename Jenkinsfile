#!/usr/bin/env groovy
library identifier: 'jenkins-shared-lib@main', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://github.com/vladibo13/jenkins-shared-libary.git',
     credentialsId: 'github-secret'
    ]
)

pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vladibo/world-of-games:latest'
    }

    stages{
        stage("build docker image") {
            steps {
                script {
                  echo "building docker image"
                  buildImage(env.IMAGE_NAME)
                  dockerLogin()
                  dockerPush(env.IMAGE_NAME)
                }
            }
        }

        stage("test") {
            steps {
                script {
                   echo "testing the app..."
                }
            }
        }

        stage("deploy") {
            steps {
                script {
                   echo "deploying the app..."
                }
            }
        }

    }
}