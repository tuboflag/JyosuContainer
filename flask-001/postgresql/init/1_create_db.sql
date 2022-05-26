create database flask_tutorial;

--ユーザーの作成
CREATE USER postgres;
--ユーザーにDBの権限をまとめて付与
GRANT ALL PRIVILEGES ON DATABASE flask_tutorial TO postgres;