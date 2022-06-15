#! /bin/bash

filename='document_to_download.tsv'

rm -rf ./corpus/raw
mkdir -p ./corpus/raw

cat $filename | while IFS=$'\t' read -r url docId title; do
    echo $docId $title
    wget -q $url -O ./corpus/raw/$title.txt
done