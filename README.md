# SIMA - Sistema de Monitoramento e Automação de Minas Gerais.

O objetivo deste repositório é documentar o nosso Sistema de Monitoramento e Automação, que gerencia os projetos do Automatiza.MG.

## Setup

[![Watch the video](https://img.youtube.com/vi/sKZJpcMSuSs/maxresdefault.jpg)](https://youtu.be/sKZJpcMSuSs)

- Clonar repositório
```$
git clone https://github.com/automatiza-mg/sima.git 
```

- Criar ambiente virtual python e instalar pacotes

```python
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

- Rodar migrações

```python
$ python manage.py migrate
```

- Criar usuário

```python
$ python manage.py createsuperuser
```

- Ligar o servidor

```python
$ $ python manage.py runserver
```
