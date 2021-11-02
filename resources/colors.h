// Created By Saabir. Unautherised claims of this project, unauthorised editing or unauthorised copying will result in legal action.

#include <strings.h>
#include <stdio.h>

void colorSet(char* color)
{
    if(strcasecmp(color, "Reset") == 0)
    {
        printf("\033[0m");
        return;
    }
    if(strcasecmp(color, "Red") == 0 || strcasecmp(color, "R") == 0)
    {
        printf("\033[0;31m");
    }
    else if(strcasecmp(color, "RedB") == 0 || strcasecmp(color, "RB") == 0)
    {
        printf("\033[1;31m");
    }
    else if(strcasecmp(color, "Green") == 0 || strcasecmp(color, "G") == 0)
    {
        printf("\033[0;32m");
    }
    else if(strcasecmp(color, "GreenB") == 0 || strcasecmp(color, "GB") == 0)
    {
        printf("\033[1;32m");
    }
    else if(strcasecmp(color, "Yellow") == 0 || strcasecmp(color, "Y") == 0)
    {
        printf("\033[0;33m");
    }
    else if(strcasecmp(color, "YellowB") == 0 || strcasecmp(color, "YB") == 0)
    {
        printf("\033[1;33m");
    }
    else if(strcasecmp(color, "Blue") == 0 || strcasecmp(color, "B") == 0)
    {
        printf("\033[0;34m");
    }
    else if(strcasecmp(color, "BlueB") == 0 || strcasecmp(color, "BB") == 0)
    {
        printf("\033[1;34m");
    }
    else if(strcasecmp(color, "Magenta") == 0 || strcasecmp(color, "M") == 0)
    {
        printf("\033[0;35m");
    }
    else if(strcasecmp(color, "MagentaB") == 0 || strcasecmp(color, "MB") == 0)
    {
        printf("\033[1;35m");
    }
    else if(strcasecmp(color, "Cyan") || strcasecmp(color, "C"))
    {
        printf("\033[0;36m");
    }
    else if(strcasecmp(color, "CyanB") == 0 || strcasecmp(color, "CB") == 0)
    {
        printf("\033[1;36m");
    }
    else
    {
        printf("\033[0m");
    }
}