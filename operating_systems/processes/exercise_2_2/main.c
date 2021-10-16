#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int main() {
    int n = 5; // number of child processes to create
    for(int i = 0; i < n; i++) {
        if(fork() == 0) {
            printf("child process pid = %d, parent process pid = %d \n", getpid(), getppid());
            _exit(0);
        }
        printf("parent process pid = %d \n", getpid());
        pid_t pid;
        if((pid = wait(&i) > 0 )) {
            if(WIFEXITED(i)) {
                printf("child process pid %d exited normally \n", pid);
            }else {
                printf("child process pid %d exited abnormally \n", pid);
            }
        }
    }
    return 0;
}
