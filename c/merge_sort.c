#include <stdio.h>
#include <string.h>
#include "sort_test.c"

int *array_copy(int dest[], int src[], int dest_start, int count)
{
    for (int i = 0; i < count; i++)
        dest[dest_start + i] = src[i];

    // print_array(dest, dest_start + count);
    // printf("\n");
    return dest;
}

int *merge(int left_part[], int right_part[], int left_size, int right_size)
{
    int l = 0;
    int r = 0;
    int left[left_size];
    int right[right_size];
    memcpy(left, left_part, left_size * 4);
    memcpy(right, right_part, right_size * 4);

    int merge_list[left_size + right_size];

    while (l < left_size && r < right_size)
    {
        if (left[l] < right[r])
        {
            merge_list[l + r] = left[l];
            l++;
        }
        else
        {
            merge_list[l + r] = right[r];
            r++;
        }
    }
    /*printf("\n");
    print_array(merge_list, l + r);
    printf("\n");
    print_array(left, left_size);
    printf("\n");
    print_array(right, right_size);
    printf("\n");*/

    if (l < left_size)
        // return array_copy(merge_list, left + l, l + r, left_size - l);
        memcpy(merge_list + l + r, left + l, (left_size - l) * 4);
    else
        // return array_copy(merge_list, right + r, l + r, right_size - r);
        memcpy(merge_list + l + r, right + r, (right_size - r) * 4);

    return merge_list;
}

int *merge_sort(int list[], int size)
{
    if (size < 2)
        return list;

    int mid = (int)size / 2;
    int left[mid];
    int right[size - mid];
    memcpy(left, list, mid * 4);
    memcpy(right, list + mid, (size - mid) * 4);
    /*printf("split starts\n");
    print_array(left, mid);
    printf("\n");
    print_array(right, size - mid);
    printf("\n");
    printf("split ends\n");*/

    int *new_left = merge_sort(left, mid);
    int *new_right = merge_sort(right, size - mid);
    /*printf("merge starts\n");
    print_array(new_left, mid);
    printf("\n");
    print_array(new_right, size - mid);
    printf("\n");
    printf("merge ends\n");*/

    return merge(new_left, new_right, mid, size - mid);
}

void main()
{
    // sort_test(merge_sort);
    int sort_list[] = {6, 1, 2, 0, 5};
    int *index = merge_sort(sort_list, sizeof(sort_list) / 4);

    print_array(index, 5);
}