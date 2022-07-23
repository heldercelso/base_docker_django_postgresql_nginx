## Introduction

It is a empty basic project to create a web-service system using the following technologies:

- Django Framework;
- Docker;
- Nginx;
- SSL letsencrypt (HTTPS);
- PostgreSQL database.

## Configuration

1. It is using SWAG container to provide Nginx with SSL certificates.
More info about it in `https://docs.linuxserver.io/general/swag`

However you can use official Nginx container if needed. Just change it in the `docker-compose.prod.yaml` file and change the variable to `NGINX_WITH_SWAG=0` in `production.env`.

2. Edit `nginx_swag_https/ssl.conf` to include the needed headers or leave it as is by default.

### Adding your domain

1. Edit .conf files:
* If Swag container is being used (default):
Open `nginx_swag_https/django_project.conf` and replace <yourdomain>.

* If Nginx will be used:
Open `nginx_http/django_project.conf` and replace <yourdomain>.

2. Put you sitemap.xml in nginx_http or nginx_swag_https (Nginx or Swag respectively)

3. Edit production.env and replace <yourdomain>

## Database Backup

It was included a backup routine to the database, it generates a compressed file in backup folder (in the project root).
It can be used to automatically create new backup (including in crontab for example).

```shell
# Backup command
$ docker-compose -f .\docker-compose.backup_db.yaml run --rm db-backup

# Restore command
$ docker-compose -f .\docker-compose.backup_db.yaml run --rm db-restore
```

## Instruções para executar:

Development mode:
```shell
$ docker-compose up
```

Production mode
```shell
$ docker-compose -f docker-compose.prod.yaml up
```