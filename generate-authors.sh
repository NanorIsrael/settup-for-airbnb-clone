#!/usr/bin/env bash

file_path="./"
# see also ".mailmap" for how email addresses and names are deduplicated
git -C "$file_path" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf >> "$file_path/AUTHORS"
