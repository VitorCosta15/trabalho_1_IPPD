# Trabalho 1 – IPPD

## Versões utilizadas

- **Linguagem C**: **gcc (GCC) 15.2.0**
- **Python**: **Python 3.11+**

> Recomenda-se o uso de gcc para compilação em C e Python 3.11 ou superior para evitar problemas de compatibilidade.

---

## Estrutura do projeto

O projeto é dividido em duas partes principais: **C** (para as tarefas utilizando OpenMP) e **Python** (para a geração dos gráficos).

### Arquivos em C

- **`*.c`**  
  Contém a implementação das funções principais em C.

- **`*.h`**  
  Arquivos de cabeçalho que declaram as funções e estruturas utilizadas nos arquivos `.c`.

- **`Makefile`**  
  Responsável por automatizar a compilação do código C.

### Arquivos em Python

- **`plot_tarefa_{C,D}.py`**  
Leitura dos csvs e geração dos gráficos.

### Arquivos csv
Localizados no diretório `data/`. Estes arquivos são criados de forma manual através dos resultados obtidos na saída dos códigos `C`.

**tarefa_C_parallel_simd.csv**

**tarefa_C_seq.csv**

**tarefa_D_variante_arrumada.csv**

**tarefa_D_variante_ingenua.csv**
---

## Como compilar e executar

### 1. Compilar o código em C

No diretório raiz do projeto, execute:

```bash
make
```
```bash
./build/omp/tarefa_C_parallel_simd
./build/omp/tarefa_C_simd
```
Válido para todos os códigos objeto em build

>Os resultados dos códigos C são impressos no terminal. Para facilitar, copiamos estas saídas e colamos em arquivos csv para serem gerados os gráficos a partir dos códigos Python. O caminho dos arquivos csv são passados diretamente através de variáveis String dentro dos arquivos Python.
---

### 2. Executar o código em Python

```bash
python3 plot_tarefa_C.py
python3 plot_tarefa_D.py

```

## Dependências

- gcc 15.2.0
- Python 3.11+
- Bibliotecas padrão da linguagem C
- Bibliotecas padrão do Python (`matplotlib`, `pandas`.)

---



