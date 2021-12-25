#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("PP process with pid = %d and ppid = %d \n", getpid(), getppid());
    if(fork() == 0) {
        printf("F1 process with pid = %d and ppid = %d \n", getpid(), getppid());
        if(fork() == 0) {
            printf("F4 process with pid = %d and ppid = %d \n", getpid(), getppid());
            char com[100];
            sprintf(com, " Ici processus %d de père %d ", getpid(), getppid());
            execl("/bin/echo", "echo", com, NULL);
        }
        wait(NULL);
        _exit(0);
    }
    if(fork() == 0) {
        printf("F2 process with pid = %d and ppid = %d", getpid(), getppid());
        if(fork() == 0) {
            printf("F5 process with pid = %d and ppid = %d \n", getpid(), getppid());
            char com[100];
            sprintf(com, " Ici processus %d de père %d ", getpid(), getppid());
            execl("/bin/echo", "echo", com, NULL);
        }
        if(fork() == 0) {
            printf("F6 process with pid = %d and ppid = %d \n", getpid(), getppid());
            char com[100];
            sprintf(com, " Ici processus %d de père %d ", getpid(), getppid());
            execl("/bin/echo", "echo", com, NULL);
        }
        wait(NULL);
        _exit(0);
    }
    if(fork() == 0) {
        printf("F3 process with pid = %d and ppid = %d \n", getpid(), getppid());
        if(fork() == 0) {
            printf("F7 process with pid = %d and ppid = %d \n", getpid(), getppid());
            char com[100];
            sprintf(com, " Ici processus %d de père %d ", getpid(), getppid());
            execl("/bin/echo", "echo", com, NULL);
        }
        wait(NULL);
        _exit(0);
    }
    return 0;
}
