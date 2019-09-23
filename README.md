# zarvis-example-flask-skaffold

Simple Hello world example using [Flask](https://palletsprojects.com/p/flask/) and [Skaffold](https://skaffold.dev). 


## Prerequisites

 - [Minikube](https://github.com/kubernetes/minikube).
 - [Skaffold](https://skaffold.dev).


## Run locally

Start [minikube](https://github.com/kubernetes/minikube) and run

```
skaffold dev --port-forward
```

And browse http://localhost:8080


## Deploy to Zarvis

 - Clone this repository
 - Install Zarvis Github App on your cloned repository
 - Select project from zarvis.ai, go to Deploy tab, and select branch to deploy.
 - Once deployed, http endpoint will be created.
 - Try promote to production in 'deploy' tab.
 - Try configure access control in 'setting' tab.
 