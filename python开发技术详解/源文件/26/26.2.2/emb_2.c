#include <Python.h>

int main(int argc, char *argv[])
{
    PyObject *pName, *pModule, *pDict, *pFunc;
    PyObject *pArgs, *pValue;
    int i;

    #�жϲ�������
    if (argc < 3) {
        fprintf(stderr,"Usage: call python_file function_name [args]\n");
        return 1;
    }