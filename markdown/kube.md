# Kubernetes

## Basic usage

1. Download kubeconfig
2. Set connection config `export KUBECONFIG=/home/matej/kube/conf.yaml`
3. Set namespace `kubectl config set-context --current --namespace <NAMESPACE>`
4. List all `kubectl get all`
5. Get pod status `kubectl get pod <POD>`
6. Get shell `kubectl exec --stdin --tty <POD> -- /bin/bash`
