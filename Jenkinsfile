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
        IMAGE_NAME = 'vladibo/world-of-games:1.1'
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
                    echo "deploying the image to ec2"
                    dockerCmd = 'docker run -p 4999:4999 -d vladibo/world-of-games:latest'
                    dockerComposeCommand = 'docker-compose -f docker-compose.yaml up --detach'
                    sshagent(['aws-ec2-key']) {
                        sh "scp docker-compose.yaml src/files/scores.txt ec2-user@54.81.204.137:/home/ec2-user/world-of-games"
                        sh "ssh -o StrictHostKeyChecking=no ec2-user@54.81.204.137 "
                        sh "cd world-of-games && ${dockerComposeCommand} && cat scores.txt"
                    }
                }
            }
        }

    }
}