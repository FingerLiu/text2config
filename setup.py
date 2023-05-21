# pacakge define of text2config
import setuptools
setuptools.setup(
    name="text2config",
    version="0.0.1",
    author="liupeng",
    author_email="liupeng.dalian@gmail.com",
    description="text to config or command",
    long_description="""Convert natural language text to configuration files(yaml/ini/conf/json) or command of various projects(docker/kubernetes/vim/nginx/postgres/terraform) with the power of Pre-Trained models.
Relieve you from the burden of remembering configuration and commands.
""",
    long_description_content_type="text/plain",
    url="https://github.com/FingerLiu/text2config",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'text2config': ['pkg/openai/templates/*.tpl']},

    install_requires=[
        "langchain",
        "openai",
        "azure-core",
        "google-search-results",
    ],
    entry_points={
        'console_scripts': [
            't2c = text2config:main'
        ]
    },

)