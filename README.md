# Cookiecutter template for Angular and Django

## Deployment
Allow `docker-compose` to access backend script
```bash
$ chmod 777 backend/docker/entrypoint.sh backend/docker/wait-for-postgres.sh
```