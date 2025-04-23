#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
mariadb-dump \
      -h mariadb_container \
      --databases ${MARIADB_DATABASE} \
      -u root -p${MARIADB_ROOT_PASSWORD} \
      > /database_admin/backups/${MARIADB_DATABASE}_bkp_${TIMESTAMP}.sql