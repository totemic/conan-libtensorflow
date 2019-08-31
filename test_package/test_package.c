#include <stdio.h>
#include <string.h>

#include <tensorflow/c/c_api.h>


int main(int argc, char *argv[])
{
    TF_Status* status = TF_NewStatus();
    TF_DeleteStatus(status);
    return 0;
}
