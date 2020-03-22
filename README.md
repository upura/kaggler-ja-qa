# kaggler-ja-qa

## Django

```
docker-compose up -d --build
```
http://localhost:8000/admin

### DB settings

```
docker-compose run web ./manage.py makemigrations
docker-compose run web ./manage.py migrate
```

## Nust.js
```
docker exec -it nuxt /bin/bash
cd front
yarn dev
```
http://localhost:3000/

## ref
- [Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)
- [フロントNuxt.js - バックDjango間のAPI連携を実装してみた](https://qiita.com/ryomatube/items/1b36fe6d73b9a6c3468c)
- [Vuetify 2.0 で datatable を使う](https://qiita.com/trustbank_kei/items/45d02313241c8235ad5e)
- [Container Registry & Runtime (Docker Deploys)](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- [Push multiple Docker images to Heroku Container Registry](https://devcenter.heroku.com/changelog-items/1191)
