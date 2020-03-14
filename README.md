# kaggler-ja-qa

## install

```
python3 -m venv env
source env/bin/activate
pip install django djangorestframework django-filter
pip install coreapi
pip install Pygments Markdown
```

## Create project and app

```
django-admin startproject kaggler_ja_qa
cd kaggler_ja_qa
python manage.py startapp faq
```

## DB settings

```
python manage.py makemigrations
python manage.py migrate
```

## ref
- [Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
