import argparse
from argparse import RawTextHelpFormatter
from langchain.prompts import PromptTemplate
from text2config.pkg.openai import prompts
from text2config.pkg.openai import quest

parser = argparse.ArgumentParser(description="""Convert natural language text to configuration files(yaml/ini/conf/json) 
or command of various projects(docker/kubernetes/vim/nginx/postgres/terraform).

Example: t2c k8s "get all pod in namespace kube-system and sort by create time"
""",
                                 formatter_class=RawTextHelpFormatter)
parser.add_argument("-m", "--mode", type=str, choices=["cmd", "config"],
                    default="cmd", help="generate command or config")
parser.add_argument("command", type=str, choices=["docker", "k8s", "kubernetes", "kubectl", "nginx"], default="kubectl", help="command name")
parser.add_argument("goal", type=str, help="goal of the command or config that you want to generate")
parser.add_argument("-c", "--config")
parser.add_argument("-d", "--debug", action="store_true", default=False, help="show debug log")


def parse_args():
    args = parser.parse_args()
    command = args.command
    goal = args.goal
    mode = args.mode
    config = args.config
    if args.debug:
        print(f"command goal mode config: {command} {goal} {mode} {config}")
    if command in ('k8s', 'kubernetes', 'kubectl'):
        command = 'k8s'
    prompt_str = f"{command}_{mode}"
    if hasattr(prompts, prompt_str):
        promptTemplate: PromptTemplate = getattr(prompts, prompt_str)
        prompt = promptTemplate.format(goal=goal)
        if args.debug:
            print(prompt)
        print(quest(prompt))



