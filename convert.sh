#!/usr/bin/env bash

source ./setenv.sh

if [ "$#" -ne 1 ] ; then
  echo "Pô Felipe, assim não dá. Você tem que por o caminho do arquivo como argumento na frente do comando. E.g.: ./convert.sh /home/Felipe/Desktop/doc.tex" >&2
  exit 1
fi

plastex --dir=./out/ --theme=custom $1

