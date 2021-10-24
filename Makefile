build:
	docker build -t k8s-log-collector:v1 .

run-docker:
	docker run -ti --rm -v ${PWD}/resources:/app/resources k8s-log-collector:v1 --log-file=./resources/cri-o.log


init:
	if [[ ! -f ~/.pyenv/versions/3.9.4/envs/k8s-log-collector/bin/activate ]]; then pyenv install 3.6.4 && pyenv virtualenv 3.9.4 k8s-log-collector && source ~/.pyenv/versions/3.9.4/envs/k8s-log-collector/bin/activate && pip install -r requirements.txt; fi

test:
	python tests.py

run-script:
	python app.py --log-file=./resources/cri-o.log
