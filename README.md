# CDL Assignment

Code execution video - [watch here](https://www.youtube.com/watch?v=Ui3gpIJ4XwQ)
<!-- ### Vanilla deployment
```bash
minikube addons enable ingress
kubectl apply -f archive/service.yaml
kubectl apply -f archive/deployment.yaml
kubectl apply -f archive/ingress.yaml

# find address from here
watch kubectl get ingress

# go to your vim /etc/hosts
# add following line (your local address would be different)
<address> app.com

# go to http://app.com/initiate and the service is triggered
``` -->

### Using Helm
```bash
minikube start --driver docker
minikube addons enable ingress
helm install sample-helm-app sample-helm-app --values ./sample-helm-app/values.yaml

# helm upgrade sample-helm-app sample-helm-app --values ./sample-helm-app/values.yaml
# helm upgrade sample-helm-app sample-helm-app --set deployment.tag=1.0.7 --values ./sample-helm-app/values.yaml

curl http://app.com/initiate

# helm uninstall sample-helm-app

```

### Prometheus
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm search repo prometheus-community
helm install prometheus prometheus-community/prometheus

# kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
# minikube service prometheus-server-ext

export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")
kubectl --namespace default port-forward $POD_NAME 9090
# access prometheus portal from localhost:9090

```