# Trabalho 1 – IPPD

**Hardware utilizado: Intel Core I5 10ª geração, notebook alimentado à tomada, 4 cores físicos, 8 cores lógicos, 8 GB ram.**

## Versões utilizadas

- **Linguagem C**: **gcc (GCC) 9.4.0**
- **Python**: **Python 3.11+**

> Recomenda-se o uso de gcc para compilação em C e Python 3.11 ou superior para evitar problemas de compatibilidade.

flag -O3 do GCC usada para compilação (ver run.sh)

---

## Estrutura do projeto

O projeto é dividido em duas partes principais: **C** (para as tarefas utilizando OpenMP) e **Python** (para a geração dos gráficos).

### Arquivos em C

- **`*.c`**  
  Contém a implementação das funções principais em C.

- **`Makefile`**  
  Responsável por automatizar a compilação do código C.

### Arquivos em Python

- **`plot_tarefa_{C,D}.py`**  
Leitura dos csvs e geração dos gráficos.

### Arquivos csv
Localizados no diretório `data/`. Estes arquivos são criados de maneira automatizada após rodar os códigos em C.

**tarefa_C_parallel_simd.csv**

**tarefa_C_simd.csv**

**tarefa_C_seq.csv**

**tarefa_D_variante_arrumada.csv**

**tarefa_D_variante_ingenua.csv**



## Como compilar e executar
Basta rodar o comando ./run.sh em um ambiente Linux, o script já automatiza tudo, desde compilar os arquivos .c, rodar os executáveis, gerar os .csv e gerar os gráficos com o pyhton.


## Recursos necessários 

- gcc 9.4.0 (versão utilizada)
- OpenMP 4.5
- Python 3.11+
- Bibliotecas padrão da linguagem C
- Bibliotecas padrão do Python (`matplotlib`, `pandas`.)

---



