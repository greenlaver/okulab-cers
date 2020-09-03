# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.7-alpine

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# ホストのrequirementsをコンテナの作業ディレクトリにコピー
COPY ./requirements.txt /usr/src/app/requirements.txt

# 必要なもの全部インストール
RUN apk update && \
    apk add postgresql-libs libxml2-dev libxslt-dev libc-dev && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

# ホストのカレントディレクトリ（現在はappディレクトリ）を作業ディレクトリにコピー
COPY . /usr/src/app/

