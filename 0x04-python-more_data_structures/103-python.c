#include <Python.h>
/**
 * print_python_list - representation of python lists with c
 * Return: void
*/

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *element;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

/**
 * print_python_bytes- Dealing with bytes using python
 * Return: void
*/
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *data = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  [.] Length: %ld\n", size);
    printf("  [.] Address of the first 10 bytes: %p\n", (void *)data);

    printf("  [.] Data: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx", data[i]);
        if (i < size - 1 && i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}
