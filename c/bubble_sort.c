#include <stdio.h>
#include "sort_test.c"

int *bubble_sort(int list[], int size);

int *bubble_sort(int list[], int size)
{

    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - 1 - i; j++)
        {
            if (list[j] > list[j + 1])
            {
                int temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }
        }
    }

    list[size] = '0';

    return list;
}

void main()
{
    /*int sort_list[] = {6, 1, 2, 0, 5};
    int *index = bubble_sort(sort_list, sizeof(sort_list) / 4);

    while (*index != '0')
    {
        printf("%d, ", *index);
        index++;
    }*/
    sort_test(bubble_sort);
}