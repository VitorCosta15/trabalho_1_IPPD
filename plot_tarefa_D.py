import pandas as pd
import matplotlib.pyplot as plt

# Arquivos CSV
csv_ingenua = "data/tarefa_D_variante_ingenua.csv"
csv_arrumada = "data/tarefa_D_variante_arrumada.csv"

# Leitura dos arquivos CSV
df_ingenua = pd.read_csv(csv_ingenua, sep=';')
df_arrumada = pd.read_csv(csv_arrumada, sep=';')

# Valores únicos de N e número de threads
Ns = sorted(df_ingenua['N'].unique())
threads_ordem = [1, 2, 4, 8, 16]

# Ordenação das colunas 'threads'
df_ingenua['threads'] = pd.Categorical(
    df_ingenua['threads'],
    categories=threads_ordem,
    ordered=True
)

df_arrumada['threads'] = pd.Categorical(
    df_arrumada['threads'],
    categories=threads_ordem,
    ordered=True
)

# Gerando gráficos para cada valor de N
for N in Ns:
    sub_ingenua = df_ingenua[df_ingenua['N'] == N].sort_values('threads')
    sub_arrumada = df_arrumada[df_arrumada['N'] == N].sort_values('threads')

    # Nome do arquivo de saída
    file_name = "graficos/tarefa_D_N=" + str(N)

    # Gerando o gráfico
    plt.figure()
    plt.plot(sub_ingenua['threads'], sub_ingenua['media'], marker='o', label='Ingênua')
    plt.plot(sub_arrumada['threads'], sub_arrumada['media'], marker='o', label='Arrumada')

    plt.xlabel("Número de threads")
    plt.ylabel("Tempo médio (s)")
    plt.title(f"Ingênua vs Arrumada (N = {N})")
    plt.legend()
    plt.grid(True)

    # Salvando o gráfico de cada N
    plt.savefig(file_name)
    plt.close()

    # Calculando a média do desvio padrão
    mean_std_ingenua = sub_ingenua['desvio_padrao'].mean()
    mean_std_arrumada = sub_arrumada['desvio_padrao'].mean()

    # Imprimindo as médias do desvio padrão
    print(f"N = {N}")
    print(f"  Média do desvio padrão (Ingênua):   {mean_std_ingenua:.6e}")
    print(f"  Média do desvio padrão (Arrumada):  {mean_std_arrumada:.6e}")
    print("-" * 50)

# =========================
# GRÁFICO FINAL (RESUMO)
# =========================

# Agrupando por número de threads (média sobre todos os Ns)
final_ingenua = (
    df_ingenua
    .groupby('threads', observed=True)['media']
    .mean()
    .reset_index()
)

final_arrumada = (
    df_arrumada
    .groupby('threads', observed=True)['media']
    .mean()
    .reset_index()
)

# Gerando o gráfico final
plt.figure()

plt.plot(
    final_ingenua['threads'],
    final_ingenua['media'],
    marker='o',
    label='Ingênua (média dos Ns)'
)

plt.plot(
    final_arrumada['threads'],
    final_arrumada['media'],
    marker='o',
    label='Arrumada (média dos Ns)'
)

plt.xlabel("Número de threads")
plt.ylabel("Tempo médio (s)")
plt.title("Resumo geral — Ingênua vs Arrumada (média sobre todos os N)")
plt.legend()
plt.grid(True)

# Salvando o gráfico final em PNG
plt.savefig(
    "graficos/tarefa_D_resumo_geral.png",
    dpi=300,
    bbox_inches="tight"
)

# Fechando a figura para liberar memória
plt.close()
