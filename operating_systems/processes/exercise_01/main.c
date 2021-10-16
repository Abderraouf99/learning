#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int main() {
    pid_t p = fork();
    // if child process
    if(p == 0) {
        printf("print from child process ,child process pid %d, parent process pid %d \n",getpid(),getppid());
        _exit(0);
    }
    printf("print from parent process, parent process pid %d, child process pid %d", getpid(), p);
    wait(NULL);
    return 0;
}
