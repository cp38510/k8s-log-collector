# k8s-log-collector
## CRI-O Log Parser
Parse CRI-O formatted logs file to Elasticsearch json format.
## Log Marshalling

Each log line should be written as a JSON document with the following schema.

```
{
    "@timestamp": "yyyy-MM-dd'T'HH:mm:ss.SSSSSSZ",
    "stream": "stdout",
    "log": "[INFO] Application is starting"
}
```
## How it use:
### Run with Docker:
```bash
#launch the local docker daemon
make build
make run-docker
or:
docker run -ti --rm -v ${PWD}/resources:/app/resources k8s-log-collector:v1 --log-file=./resources/cri-o.log
```
### Run without Docker:
#### Install modules:
```
pyenv install 3.6.4
pyenv virtualenv 3.9.4 k8s-log-collector
source ~/.pyenv/versions/3.9.4/envs/k8s-log-collector/bin/activate
pip install -r requirements.txt
```
#### Run script:
```
python tests.py
python app.py --log-file=./resources/cri-o.log
```
or with Makefile:
```
make init
make test
make run
```
