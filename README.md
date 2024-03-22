# Software MDC

Este é um simples projeto de software que calcula o Máximo Divisor Comum (MDC) de dois números usando o algoritmo de Euclides.

## Passos para Executar o Projeto

1. **Clone o Repositório:**

```
git clone https://github.com/seu-usuario/meu_software.git
```

2. **Navegue até o Diretório do Projeto:**

```
cd meu_software
```

3. **Instale as Dependências:**

```
pip install -r requirements.txt
```

4. **Execute o Projeto:**

```
python main.py
```

5. **Criar o Pacote do Software:**

```
pyinstaller --onefile main.py
```

6. **Navegue até o Diretório de Distribuição:**

```
cd dist/main
```

7. **Execute o Software:**

```
./main.exe
```

## Requisitos

- Python 3.x
- Bibliotecas listadas em requirements.txt

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).


# Como realizar um projeto assim:

## Estrutura:

```
meu_software/
├── LICENSE
├── README.md
├── main.py
├── main.spec
├── requirements.txt
├── setup.py
└── interface_grafica/
    ├── __init__.py
    └── views.py
└── tests/
    ├── __init__.py
    ├── test_main.py
    └── test_views.py
```

```
mkdir -p meu_software/interface_grafica && touch meu_software/main.py meu_software/interface_grafica/__init__.py meu_software/interface_grafica/views.py
```

## Criar um ambiente virtual:

```
python -m venv env
```

## Ativar o ambiente virtual:

```
source env/bin/activate
```

## Instalar as dependências:

```
pip install pyinstaller
```

## Criar o arquivo de especificação (.spec):

```
pyi-makespec main.py
```

## Compilar o programa:

```
pyinstaller main.spec
```

Após a conclusão deste último comando, você encontrará o executável do seu software na pasta dist, pronto para ser distribuído e instalado em qualquer máquina Windows. Certifique-se de testar o executável em diferentes ambientes para garantir que funcione conforme o esperado antes de distribuí-lo.