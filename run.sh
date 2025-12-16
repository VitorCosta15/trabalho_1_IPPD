#!/bin/bash

# Criar pasta data caso não exista
mkdir -p data

#Deixar liberadade ao OpenMP de distribuir o trabalho das threads
# export OMP_PROC_BIND=true
# export OMP_PLACES=cores

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
echo "Gerando gráficos" 
python3 plot_tarefa_C.py > "graficos/desvio_padrão_tarefa_C.txt"
python3 plot_tarefa_D.py > "graficos/desvio_padrão_tarefa_D.txt"

