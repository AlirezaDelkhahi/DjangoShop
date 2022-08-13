## Django Shop Backend
### 1- build backend docker image

```shell script
docker build . -t shop_backend
```

### 2- run backend and db services with docker-compose
```shell script
 docker-compose up -d
```

### 3- create admin user with:
```shell script
 docker-compose run shop_backend createsuperuser
```