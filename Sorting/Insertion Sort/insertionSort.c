#include <stdio.h>
#include <stdlib.h>


void insertionSort(int* arr, int len) {
    for (int i = 1; i < len; i++) {
        int j = i - 1;

        while (j >= 0 && arr[j + 1] < arr[j]) {
            int tmp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = tmp;

            j--;
        }
    }
}

int main() {
    int *arr = NULL, len;

    printf("Enter Count of Elements in an Array:- ");
    scanf("%d", &len);

    arr = (int *)malloc(len * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        exit(1); // Exit the Program on Allocation Failure
    }

    for (int i = 0; i < len; i++) {
        printf("Enter Elements at %d:- ", i + 1);
        scanf("%d", &arr[i]);
    }

    insertionSort(arr, len);

    printf("\nSorted Array:- ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 1;
}
