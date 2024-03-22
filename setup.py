from setuptools import setup, find_packages

setup(
    name='software_MDC',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Coloque as dependências aqui
    ],
    entry_points={
        'console_scripts': [
            'main=software_MDC.main:main',
        ],
    },
    author='Daniel Gehlen',
    author_email='harmonia251251@gmail.com',
    description='Software que calcula MDC de Euclides.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Daniel-Gehlen/py_software_MDC',
    license='MIT',
)
