#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>

long Ns[] = {100000, 500000, 1000000};
int thread_list[] = {1, 2, 4, 8, 16};

double mean(double *v, int n) {
    double s = 0.0;
    for (int i = 0; i < n; i++) s += v[i];
    return s / n;
}

double desvio_padrao(double *v, int n, double m) {
    double s = 0.0;
    for (int i = 0; i < n; i++) s += (v[i] - m) * (v[i] - m);
    return sqrt(s / n);
}

int main() {
    // CSV header
    printf("N;threads;media;desvio_padrao\n");

    for (int n_i = 0; n_i < 3; n_i++) {
        long N = Ns[n_i];

        double *A = malloc(sizeof(double) * N);
        double *B = malloc(sizeof(double) * N);

        for (long i = 0; i < N; i++) {
            A[i] = 1.0;
            B[i] = 2.0;
        }

        for (int t_i = 0; t_i < 5; t_i++) {
            int T = thread_list[t_i];
            omp_set_num_threads(T);

            double times[10];

            for (int r = 0; r < 10; r++) { //Mesma coisa aqui 10 reps por ponto

                double t1 = omp_get_wtime();
                
                #pragma omp parallel for
                for (long i = 0; i < N; i++)
                    A[i] = A[i] * 2.0 + 1.0;
                
                #pragma omp parallel for
                for (long i = 0; i < N; i++)
                    B[i] = B[i] + A[i];

                double t2 = omp_get_wtime();
                times[r] = t2 - t1;
            }

            double m = mean(times, 10);
            double sd = desvio_padrao(times, 10, m);

            printf("%ld;%d;%.8f;%.8f\n", N, T, m, sd);
        }

        free(A);
        free(B);
    }

    return 0;
}
