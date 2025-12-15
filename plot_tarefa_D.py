import pandas as pd
import matplotlib.pyplot as plt


csv_ingenua = "data/tarefa_D_variante_ingenua.csv"
csv_arrumada = "data/tarefa_D_variante_arrumada.csv"


df_ingenua = pd.read_csv(csv_ingenua, sep=';')
df_arrumada = pd.read_csv(csv_arrumada, sep=';')


Ns = sorted(df_ingenua['N'].unique())
threads_ordem = [1, 2, 4, 8, 16]


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


for N in Ns:
    sub_ingenua = df_ingenua[df_ingenua['N'] == N].sort_values('threads')
    sub_arrumada = df_arrumada[df_arrumada['N'] == N].sort_values('threads')

    file_name = "graficos/tarefa_D_N=" + str(N)

    plt.figure()
    plt.plot(sub_ingenua['threads'], sub_ingenua['media'], marker='o', label='Ingênua')
    plt.plot(sub_arrumada['threads'], sub_arrumada['media'], marker='o', label='Arrumada')

    plt.xlabel("Número de threads")
    plt.ylabel("Tempo médio (s)")
    plt.title(f"Ingênua vs Arrumada (N = {N})")
    plt.legend()
    plt.grid(True)

    
    plt.savefig(file_name)

    
    mean_std_ingenua = sub_ingenua['desvio_padrao'].mean()
    mean_std_arrumada = sub_arrumada['desvio_padrao'].mean()

    print(f"N = {N}")
    print(f"  Média do desvio padrão (Ingênua):   {mean_std_ingenua:.6e}")
    print(f"  Média do desvio padrão (Arrumada):  {mean_std_arrumada:.6e}")
    print("-" * 50)
