#include <stdio.h>
#include <stdlib.h>


int partition(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;

            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }

    int temp = arr[high];
    arr[high] = arr[i + 1];
    arr[i + 1] = temp;

    return i + 1;
}

void quickSort(int* arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
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

    quickSort(arr, 0, len - 1);

    printf("\nSorted Array:- ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 1;
}
