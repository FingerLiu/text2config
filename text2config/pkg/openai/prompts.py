import pkg_resources
from langchain.prompts import PromptTemplate

# TODO use chain and tools
__all__ = ['docker_cmd', 'k8s_cmd', 'k8s_config', 'nginx_config']

class PromptTemplateFromFile(PromptTemplate):
    # init PromptTemplate from file
    def __init__(self, input_variables, template_file):
        with open(template_file, 'r') as f:
            template = f.read()
        super().__init__(input_variables=input_variables, template=template)

docker_cmd = PromptTemplateFromFile(
    input_variables=["goal"],
    template_file=pkg_resources.resource_filename("text2config", "pkg/openai/templates/docker.tpl")
)

k8s_cmd = PromptTemplateFromFile(
    input_variables=["goal"],
    template_file=pkg_resources.resource_filename("text2config", "pkg/openai/templates/k8s-cmd.tpl")
)

k8s_config = PromptTemplateFromFile(
    input_variables=["goal", "config"],
    template_file=pkg_resources.resource_filename("text2config", "pkg/openai/templates/k8s-yaml.tpl")
)

nginx_config = PromptTemplateFromFile(
    input_variables=["goal", "config"],
    template_file=pkg_resources.resource_filename("text2config", "pkg/openai/templates/nginx.tpl")
)

