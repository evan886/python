#include <Python.h>

int main(int argc, char *argv[])
{
    Py_Initialize ();

    #����ִ�в����е����
    PyRun_SimpleString("from time import sleep\n"
                     "print ��sleep 1s��\n"
                     "sleep(1)\n");

    Py_Finalize();

    return 0;
}
