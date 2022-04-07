FROM php:7.4.9-fpm

COPY php.ini /usr/local/etc/php/

# 修正箇所
RUN apt update \
  && apt install -y default-mysql-client \
  && docker-php-ext-install pdo_mysql

WORKDIR /var/www