#!/bin/bash


host="$1"
username="$2"
password="$3"
command="$4"

until psql -h "$host" -U "$username" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

exec $command