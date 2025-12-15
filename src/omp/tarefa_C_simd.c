#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

double mean(double *v, int n){ 
    double s=0;
    for(int i=0;i<n;i++) 
        s+=v[i];
    return s/n;
    }


double stddev(double *v,int n){
    double m=mean(v,n),s=0;
    for(int i=0;i<n;i++) 
        s+=(v[i]-m)*(v[i]-m);
    return sqrt(s/n); 
    }

int main(){
    long Ns[] = {100000,500000,1000000, 10000000};
    int nN = 4, reps = 10; //Estou fazendo 10 reps por ponto, pq ta variando mto os resultados e dps tiro a média.
                           //Optei por testar tbm pra N=10000000, pra ver como se comporta com um N maior do que os testados (especialmente a variante SIMD)

    printf("versao;N;media;desvio_padrao\n");

    for(int k=0;k<nN;k++){
        long N = Ns[k];
        double tempos[reps];

        float *x = malloc(N*sizeof(float));
        float *y = malloc(N*sizeof(float));
        float a = 2.0f;

        for(long i=0;i<N;i++){ 
            x[i]=1.0; 
            y[i]=1.0; 
        }

        for(int r=0;r<reps;r++){
            double t0 = omp_get_wtime();
            #pragma omp simd
            for(long i=0;i<N;i++)
                y[i]=a*x[i]+y[i];
            double t1 = omp_get_wtime();
            tempos[r] = t1-t0;
        }

        printf("SIMD;%ld;%.8f;%.8f\n",N,mean(tempos,reps),stddev(tempos,reps));

        free(x); free(y);
    }
}
