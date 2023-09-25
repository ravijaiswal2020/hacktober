#include <stdio.h>

int main()
{
    int a[10][10],b[10][10],c[10][10],n,i,j,k;
    printf("Enter the value of N:\n");
    scanf("%d",&n);
    printf("Enter th elements in Matrix A:\n");

    for (i=0;i<n;i++){
        for (j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    printf("Enter th elements in Matrix B:\n");

    for (i=0;i<n;i++){
        for (j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for (i=0;i<n;i++){
        for (j=0;j<n;j++){

            c[i][j] = 0;
            for (k=0;k<n;k++){
                c[i][j] += a[i][j]*b[i][j];
            }
        }
    }
    printf("The product of two matrices are: \n");
    for (i=0;i<n;i++){
        for (j=0;j<n;j++){
            printf("%d\t",c[i][j]);
        }
        printf("\n");
    }

    return 0;


}
