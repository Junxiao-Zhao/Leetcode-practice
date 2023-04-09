#include <stdio.h>
#include "sort_test.c"

int *select_sort(int list[], int size);

int *select_sort(int list[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int temp_min = i;
        for (int j = i; j < size; j++)
        {
            if (list[j] < list[temp_min])
                temp_min = j;
        }
        int temp = list[temp_min];
        list[temp_min] = list[i];
        list[i] = temp;
    }

    return list;
}

void main()
{
    sort_test(select_sort);
}