#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define RED(string) "\x1b[31m" string "\x1b[0m"
const int tamanho = 100;


typedef struct {
  int *array;
  size_t used;
  size_t size;
} Array;

void initArray(Array *a, size_t initialSize) {
  a->array = malloc(initialSize * sizeof(int));
  a->used = 0;
  a->size = initialSize;
}

void insertArray(Array *a, int element) {
  // a->used is the number of used entries, because a->array[a->used++] updates a->used only *after* the array has been accessed.
  // Therefore a->used can go up to a->size 
  if (a->used == a->size) {
    a->size *= 2;
    a->array = realloc(a->array, a->size * sizeof(int));
  }
  a->array[a->used++] = element;
}

void freeArray(Array *a) {
  free(a->array);
  a->array = NULL;
  a->used = a->size = 0;
}

int notin(int a[], int b, int n)
{
    int i;
    int in;
    in = 0;
    for(i=0;i<=n;i++)
    {
        if(a[i] == b)
        {
            in = 1;
        }
    }
    return in;
}

int digitCounter(int n)
{
    int count = 0;
    if(n==0)
    {
        printf("Cant calculate the middlesquare of null");
        return 0;
    }
    else
    {
        while (n != 0)
        {
            n = n/10;
            count++;
        }
    }
    printf("\nNumber with %d digits\n",count);
    return count;
}

unsigned long middleSquare(int n, int digit)
{
    unsigned long nextNum = 0;
    unsigned long sqn = n*n;
    int trim;
    int n_middle;

    digit = digitCounter(n);
    n_middle = digit/2;
    trim = pow(10, n_middle);
    sqn = sqn/trim;
    for(int i = 0;i<digit;i++)
    {
        nextNum += (sqn % trim) * pow(10, i);
        sqn = sqn/10;
    }
    printf("Processed the number: "RED("%d")".\nIts square is: "RED("%d"), n, nextNum);
    return nextNum;
}


int main()
{
    Array a;
    int i;

    int seed_number;
    int number;
    int counter = 0;
    int already_seen[100];
    int valida;
    int digit;

    initArray(&a, 5);
    //Deixando o programa bonitinho
    printf("--------Calculadora do Método do Quadrado do meio---------");
    //Pedindo para o user digitar a seed
    printf("\nDigite a quantidade de dígitos:\n");
    scanf("%d",&digit);
    printf("\nDigite a semente a ser utilizada no algoritmo:\n");
    scanf("%d",&seed_number);
    number = seed_number;
    printf("\nCalculando a semente: " RED("%d") " \n",seed_number);
    //Looping the algorithm
    while (counter<8)
    {
        number = middleSquare(number, digit);
        insertArray(&a, number);
        counter++;
    }
    printf("\nPrinting the vector: \n");
    for(i=0;i<=counter;i++)
    {
        printf("Position %d: %d\n",i,a.array[i]);
    }
    //indicando que o programa acabou
    return 0;
}