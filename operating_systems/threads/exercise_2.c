#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>

void *threadCallBack(void *x)
{
    printf("thread has thread-id %d and is attached to process %d \n", pthread_self(), getpid());
    char *messageToMainThread = malloc(40);
    sprintf(messageToMainThread, "Here is thread with thread_id = %d", pthread_self());
    pthread_exit((void *)messageToMainThread);
}

int main()
{
    char numberOfThreads = 4;
    pthread_t *tid = malloc(numberOfThreads * sizeof(pthread_t));

    for (int i = 0; i < numberOfThreads; i++)
    {
        pthread_create(&tid[i], NULL, threadCallBack, NULL);
    }
    printf("main thread with tid = %d attached to process pid = %d \n", pthread_self(), getpid());
    for (int i = 0; i < numberOfThreads; i++)
    {
        char *messageFromThread;
        pthread_join(tid[i], (void **)&messageFromThread);
        printf("%s \n", messageFromThread);
        free(messageFromThread);
    }
    return 0;
}