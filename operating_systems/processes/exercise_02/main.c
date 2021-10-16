#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int n = 5;
    pid_t p;
    while((p = fork()) > 0 && n > 0) {
        n--;
    }
    if(p == 0) {
        printf("child pid %d, parent pid %d\n", getpid(), getppid());
    }else {
        printf("parent pid %d \n",getpid());
        wait(NULL);
    }
    return 0;
}
