from setuptools import setup, find_packages

setup(
    name='moake_client_python',
    version='0.0.1',
    description='The Moake Client for Python',
    url='https://github.com/LegendaryAI/moake_client_python',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['requests']
)
