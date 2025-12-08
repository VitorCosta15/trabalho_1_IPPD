#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>


double mean(double *v, int n){
    double s=0; for(int i=0;i<n;i++) s+=v[i];
    return s/n;
}

double stddev(double *v, int n){
    double m = mean(v,n),s=0;
    for(int i=0;i<n;i++) s+=(v[i]-m)*(v[i]-m);
    return sqrt(s/n);
}

int main(){
    long Ns[] = {100000,500000,1000000};
    int nN = 3, reps = 5;

    printf("versao,N,mean,desvio_padrao\n");

    for(int k=0;k<nN;k++){
        long N = Ns[k];
        double tempos[reps];

        float *x = malloc(N*sizeof(float));
        float *y = malloc(N*sizeof(float));
        float a = 2.0f;

        for(long i=0;i<N;i++){ x[i]=1.0; y[i]=1.0; }

        for(int r=0;r<reps;r++){
            double t0 = omp_get_wtime();
            for(long i=0;i<N;i++)
                y[i] = a*x[i] + y[i];
            double t1 = omp_get_wtime();
            tempos[r]=t1-t0;
        }

        printf("SEQ,%ld,%.8f,%.8f\n",N,mean(tempos,reps),stddev(tempos,reps));

        free(x); free(y);
    }
}
