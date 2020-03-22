FROM node:latest

RUN mkdir -p /code

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=development

# yarnとaxiosをinstall
RUN yarn install
RUN yarn add @nuxtjs/axios

# ディレクトリを移動する
WORKDIR /code

# ポート3000番を開放する
EXPOSE 3000
