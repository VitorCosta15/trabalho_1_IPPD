## Relatório

O hardware utilizado nos experimentos possui 4 núcleos e 8 threads.

### Tarefa C - Vetorização com simd

Utiliza a diretiva #pragma omp simd. Essa diretiva permite a execução simultânea de múltiplas iterações dos laços associados por meio de instruções SIMD. 
Referência: https://www.openmp.org/spec-html/5.0/openmpsu42.html

A partir da analise do gráfico `graficos/tarefa_C_seq_vs_simd.png`, a implementação SIMD (que utiliza a diretiva #pragma omp simd para usar instruções vetoriais do processador, como AVX, conforme apresentado pelo professor em aula) é mais rápida do que a execução sequencial quando o N é grande.

### Tarefa D
Utiliza dois casos: o primeiro é chamada de "ingênua", onde são declarados dois `omp parallel for`; O segundo, chamada de "arrumada", utiliza uma região `omp parallel` e dentro desta região, dois `omp parallel for`. O foco destas duas versões é avaliar o overhead de sincronização. Referência: https://www.openmp.org/spec-html/5.0/openmpse14.html

A partir da analise do gráfico `graficos/tarefa_D_resumo_geral.png.png`, podemos notar que a versão "arrumada" foi a com menor custo de tempo em relação à "ingênua", sendo mais consistente quando o N é maior. A vantagem principal é que as threads são criadas apenas uma vez e permanecem ativas para executar o trabalho de ambos os loops, o que reduz drasticamente o custo de gerenciamento e sincronização.

## Conclusão
Os resultados mostram que ganhos significativos de desempenho em álgebra linear e processamento vetorial dependem de duas estratégias principais. A tarefa C, que faz o uso de vetorização SIMD, que explora eficientemente o hardware e supera a execução sequencial, sobretudo para grandes volumes de dados; e a tarefa D, que demonstra a diferença do overhead de paralelismo entre duas técnicas, evidenciada pela superioridade da versão arrumada em relação à ingênua. Manter as threads ativas ao longo da execução minimiza custos de criação e sincronização, tornando a paralelização mais eficiente.

