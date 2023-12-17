// Parse command line arguments for basic user flow. 
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){
    if(argc < 2){
        printf("Please provide an argument\n");
        return 1;
    }
    if(strcmp(argv[1], "send")==0) // User specified "send" 
    {
        system("python3 send_email.py");
    }
    else if(strcmp(argv[1], "config")==0) // User specified "config"
    {
        system("python3 config.py");
    }
    else if(strcmp(argv[1], "help")==0) // User specified "help" 
    {
        printf("Usage: ./command_parser [command]\n");
        printf("Commands:\n");
        printf("send\t\tSend an email\n");
        printf("config\t\tConfigure email settings\n");
        printf("help\t\tDisplay this help message\n");
    }
    else{
        printf("Invalid command\n");
        return 1;
    }
    return 0;
}
