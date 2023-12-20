# Openshift Flask Deployment Test
This is test for deploying simple flask app on openshift kubernetes cluster

## OC commands for deployment
oc new-app --name=flask-hello-world python:3.12.0-slim~https://github.com/JuJu2181/flask-hello-world.git

oc expose pod flask-hello-world-7f49bc6f9f-qmfck --port=5000 --name=flask-hello-world-service

oc create route edge --service=flask-hello-world-service --port=5000 

