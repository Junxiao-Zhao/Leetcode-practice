#include <stdio.h>
#include <string.h>

void print_array(int l[], int size)
{
    int *list;
    memcpy(list, l, size * 4);
    for (int i = 0; i < size; i++)
    {
        printf("%d, ", *(list + i));
    }
}

void sort_test(int *(*func)(int[], int))
{
    int sort_list[] = {6, 1, 2, 0, 5};
    int *index = (*func)(sort_list, sizeof(sort_list) / 4);

    print_array(index, 5);
}