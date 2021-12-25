#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void onCancelCallback(int signalNumber)
{
    printf("Received signal %d SIGINT = %d \n", signalNumber, SIGINT);
}
int main()
{
    int pid = fork();
    if (pid == 0)
    {
        // child process;
        signal(SIGINT, onCancelCallback);
        printf("child process running \n");
        // _exit(0);
    }
    // wait(NULL);
    // replaces the original callback by the new callback for the SIGINT signal (CTRL + c)
    printf("process pid = %d \n", getpid());
    int killValue = kill(pid, SIGKILL);
    printf("parent process killed child process \n");
    printf("kill value %d \n", killValue);
    return 0;
}