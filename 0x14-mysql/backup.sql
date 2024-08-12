#!/usr/bin/env bash
# Bash script that generates a MySQL dump and creates a compresse#d archive out of it.

mysqldump -uroot -p"$1" --all-databases > backup.sql
tar -cvzf "$(date +%d-%m-%Y)".tar.gz backup.sql