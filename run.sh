#!/bin/bash

# Criar pasta data caso não exista
mkdir -p data


for exe in build/seq/*; do
    if [[ -x "$exe" && ! -d "$exe" ]]; then
        filename=$(basename "$exe")
        output="data/${filename}.csv"

        echo "Rodando seq -> $filename  |  output: $output"
        "$exe" > "$output"
    fi
done

for exe in build/omp/*; do
    if [[ -x "$exe" && ! -d "$exe" ]]; then
        filename=$(basename "$exe")
        output="data/${filename}.csv"

        echo "Rodando omp -> $filename  |  output: $output"
        "$exe" > "$output"
    fi
done

