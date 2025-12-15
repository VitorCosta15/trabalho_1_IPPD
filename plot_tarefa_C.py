import pandas as pd
import matplotlib.pyplot as plt


seq_csv = "data/tarefa_C_seq.csv"
simd_csv = "data/tarefa_C_simd.csv"
parsimd_csv = "data/tarefa_C_parallel_simd.csv"


df_seq = pd.read_csv(seq_csv, sep=';')
df_simd = pd.read_csv(simd_csv, sep=';')
df_par = pd.read_csv(parsimd_csv, sep=';')

Ns = df_seq['N'].values

plt.figure()
plt.plot(df_seq['N'], df_seq['media'], marker='o', label='SEQ')
plt.plot(df_simd['N'], df_simd['media'], marker='o', label='SIMD')

plt.xlabel("N")
plt.ylabel("Tempo médio (s)")
plt.title("Tarefa C — SEQ vs SIMD")
plt.legend()
plt.grid(True)

plt.savefig("graficos/tarefa_C_seq_vs_simd.png")
plt.close()

print("SEQ vs SIMD")
print(f"  Média desvio padrão SEQ : {df_seq['desvio_padrao'].mean():.6e}")
print('-'*50)
print(f"  Média desvio padrão SIMD: {df_simd['desvio_padrao'].mean():.6e}")
print('-'*50)


threads_ordem = [1, 2, 4, 8, 16]

for N in sorted(df_par['N'].unique()):
    sub_par = df_par[df_par['N'] == N].sort_values('threads')

    mean_seq = df_seq[df_seq['N'] == N]['media'].values[0]
    mean_simd = df_simd[df_simd['N'] == N]['media'].values[0]

    plt.figure()

    
    plt.plot(
        sub_par['threads'],
        sub_par['media'],
        marker='o',
        label='PAR-SIMD'
    )

    # Pontos SEQ e SIMD to colocando sobre thread=1 pq n exploram paralelismmo em thread 
    plt.scatter(
        [1], [mean_seq],
        marker='s',
        color = "orange",        
        s=80,
        label='SEQ'
    )

    plt.scatter(
        [1], [mean_simd],
        marker='^',
        color = "green",
        s=80,
        label='SIMD'
    )

    plt.xlabel("Número de threads")
    plt.ylabel("Tempo médio (s)")
    plt.title(f"PAR-SIMD vs SIMD vs SEQ (N = {N})")
    plt.legend()
    plt.grid(True)

    plt.savefig(f"graficos/tarefa_C_parallel_simd_N_{N}.png")
    plt.close()

    print(f"N = {N}")
    print(f"  Média desvio padrão PAR-SIMD: {sub_par['desvio_padrao'].mean():.6e}")
    print("-" * 50)
