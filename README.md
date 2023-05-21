# text to config or command (t2c)
Convert natural language text to configuration files(yaml/ini/conf/json) or command of various projects(docker/kubernetes/vim/nginx/postgres/terraform) with the power of Pre-Trained models.
Relieve you from the burden of remembering configuration and commands.

# Install
## from pypi 
**not supported yet,due to pypi server closed package uploading**
```bash
# pip install text2config
```
## from github
```bash
git clone https://github.com/FingerLiu/text2config.git
cd text2config
pip install -e .
```
# config and run
```bash
export OPENAI_API_KEY="YOUR-KEY"

# default to 0
export OPENAI_TEMPERATURE="0"

t2c k8s "get all pod in namespace kube-system and sort by create time"

t2c docker "run image nginx:latest and mount ~/nginx.conf to /etc/nginx.conf, and also expose 80 to local 8080, remove it after stop"
```

## Tips for Chinese users
Due to network issues, you need to config proxy for openai api in your terminal like this.
```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
```
# Usage
```bash
usage: t2c [-h] [-m {cmd,config}] [-c CONFIG] [-d] {docker,k8s,kubernetes,kubectl,nginx} goal

Convert natural language text to configuration files(yaml/ini/conf/json) 
or command of various projects(docker/kubernetes/vim/nginx/postgres/terraform).

Example: t2c k8s "get all pod in namespace kube-system and sort by create time"

positional arguments:
  {docker,k8s,kubernetes,kubectl,nginx}
                        command name
  goal                  goal of the command or config that you want to generate

options:
  -h, --help            show this help message and exit
  -m {cmd,config}, --mode {cmd,config}
                        generate command or config
  -c CONFIG, --config CONFIG
  -d, --debug           show debug log

```
# Features
- [*] text to docker command
- [*] text to k8s command
- [] text to k8s yaml
- [] text to nginx conf
- [] text to any command/config with predefined prompt template.
- [] text to custom command/config with user provide prompt template
## text to docker command
```bash
t2c docker "run image nginx and export port 80 to local port 8080"

## text to k8s cmd
```bash
t2c k8s "scale deploy nginx to 3"
t2c k8s -m cmd "get svc in ns which expose domain t2c.io"
```

## text to k8s yaml
```bash
t2c k8s --mode config "run nginx deploy and export a ingress with domain t2c.github.io"
t2c k8s -m config "mount a nas pvc to deploy mysql in namespace test"
```
## text to nginx conf
```
t2c nginx -c /path/to/nginx.conf add location /docs/ to vhost t2c.io redirect to t2c.github.io
```

## Thanks
- [kubectl-ai](https://github.com/sozercan/kubectl-ai)
- [Kubectl-GPT](https://github.com/abhishek-ch/Kubectl-GPT)
