#include <stdio.h>
#include "sort_test.c"

int *insert_sort(int list[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int j = i;
        int cur = list[i];
        while (j > 0 && cur < list[j - 1])
        {
            list[j] = list[j - 1];
            j--;
        }
        list[j] = cur;
    }

    return list;
}

void main()
{
    sort_test(insert_sort);
}