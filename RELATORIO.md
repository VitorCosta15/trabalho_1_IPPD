## Relatório

O hardware utilizado nos experimentos possui 4 núcleos e 8 threads.
Foi habilitado export OMP_PROC_BIND=true e export OMP_PLACES=cores habilitando afinidade explícita de threads, fixando as threads OpenMP em núcleos físicos, reduzindo migração entre núcleos.


### Tarefa C - Vetorização com simd

Utiliza a diretiva #pragma omp simd. Essa diretiva permite a execução simultânea de múltiplas iterações dos laços associados por meio de instruções SIMD. 
Referência: https://www.openmp.org/spec-html/5.0/openmpsu42.html

A partir da analise do gráfico `graficos/tarefa_C_seq_vs_simd.png`, a implementação SIMD (que utiliza a diretiva #pragma omp simd para usar instruções vetoriais do processador, como AVX, conforme apresentado pelo professor em aula) é mais rápida do que a execução sequencial quando o N é grande.

Nota-se, nos resultados de par-simd que, apesar de a plataforma experimental possuir 8 processadores lógicos, observa-se que o pior desempenho ocorre consistentemente para T = 8. Esse comportamento é explicado pelo fato de a máquina possuir apenas 4 núcleos físicos, sendo os demais núcleos lógicos providos por SMT (Simultaneous Multithreading). Para T ≤ 4, cada thread é mapeada para um núcleo físico distinto, explorando paralelismo real. Entretanto, em T = 8, duas threads passam a competir pelos mesmos recursos de cada núcleo físico, incluindo unidades vetoriais, registradores e níveis privados de cache. Como o kernel avaliado é intensivo em SIMD e apresenta baixo número de stalls, o uso de SMT não traz benefícios e resulta em contenção de recursos, degradando o desempenho.

Curiosamente, ao aumentar o número de threads para T=16, observa-se uma melhora relativa em relação a T=8. Esse efeito não indica escalabilidade real, mas decorre de mudanças no escalonamento do sistema operacional e do runtime OpenMP, que podem favorecer uma melhor sobreposição de latências de memória e variações no mapeamento das threads aos núcleos físicos. Ainda assim, o desempenho para T=16 permanece inferior ou apenas marginalmente superior ao obtido com T=4, reforçando que o limite prático de escalabilidade para este tipo de kernel é determinado pelo número de núcleos físicos disponíveis.

Este comportamento está diretamente relacionado com as diretivas habilitadas OMP_PROC_BIND=true e OMP_PLACES=cores.

### Tarefa D
Utiliza dois casos: o primeiro é chamada de "ingênua", onde são declarados dois `omp parallel for`; O segundo, chamada de "arrumada", utiliza uma região `omp parallel` e dentro desta região, dois `omp parallel for`. O foco destas duas versões é avaliar o overhead de sincronização. Referência: https://www.openmp.org/spec-html/5.0/openmpse14.html

A partir da analise do gráfico `graficos/tarefa_D_resumo_geral.png.png`, podemos notar que a versão "arrumada" foi a com menor custo de tempo em relação à "ingênua", sendo mais consistente quando o N é maior. A vantagem principal é que as threads são criadas apenas uma vez e permanecem ativas para executar o trabalho de ambos os loops, o que reduz o custo de gerenciamento e sincronização.

## Conclusão
Os resultados mostram que ganhos significativos de desempenho em álgebra linear e processamento vetorial dependem de duas estratégias principais. A tarefa C, que faz o uso de vetorização SIMD, que explora eficientemente o hardware e supera a execução sequencial, sobretudo para grandes volumes de dados; e a tarefa D, que demonstra a diferença do overhead de paralelismo entre duas técnicas, evidenciada pela superioridade da versão arrumada em relação à ingênua. Manter as threads ativas ao longo da execução minimiza custos de criação e sincronização, tornando a paralelização mais eficiente.

