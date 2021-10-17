#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
long a = 0;
void *increment(void *x)
{
    for (int i = 0; i < 1000000; i++)
        a = a + (long)x;
    return NULL;
}
int main(int argc, char *argv[])
{
    // thread tables
    pthread_t tid[3];
    for (int i = 0; i < 3; i++)
    {
        // creating the threads     // call back is increment function and we pass 1 as param to increment
        pthread_create(&tid[i], NULL, increment, (void *)1);
    }
    // when the threads start executing we have a concurrance issue since all threads access a in reading and writing
    for (int i = 0; i < 3; i++)
        pthread_join(tid[i], NULL);
    printf(" a = %ld\n", a);
    return 0;
}