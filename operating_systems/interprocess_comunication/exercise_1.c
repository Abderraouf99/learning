#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
int main(int argc, char *argv[])
{
    if (argc != 2)
        _exit(1);
    int fd[2];        // variable for the file descriptors
    char buf;         // buffer
    pipe(fd);         // creation of unnamed pipe
    if (fork() == 0)  // case it is the child process
    {                 // le fils est un lecteur
        close(fd[1]); // closes the writing so it in read mode
        while (read(fd[0], &buf, 1) > 0)
        { // while receiving value put them in the buffer and write the buffer to the standard out (screen)
            write(1, &buf, 1);
        }
        // flushes the std out buffer
        write(1, "\n", 1);
        close(fd[0]); // close the reading head
    }
    else
    {                 // le père est  un écrivain
        close(fd[0]); // closes the reading head mean the father is in writing
        // write in the buffer the values received from the execution
        write(fd[1], argv[1], strlen(argv[1]) + 1);
        close(fd[1]); // closes the pipe and causes it to be deleted
        wait(NULL);   // attend la fin de son fils
    }
    _exit(0);
}