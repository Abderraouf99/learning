#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>
int main()
{
    // creating the file exercise-2.txt in create, write, and truncate
    int fd = open("exercise-2.txt", O_CREAT | O_WRONLY | O_TRUNC);
    dup2(fd, 1);
    close(fd);
    execlp("ls", "ls", "-l", NULL);
    return 0;
}