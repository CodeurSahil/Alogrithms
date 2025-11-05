#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int* arr, int len) {
    for (int i = 0; i < len - 1; i++) {
        
        // Add a flag to check for swaps
        int swapped = 0; 
        
        for (int j = 0; j < len - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
                
                // If we swap, set the flag
                swapped = 1; 
            }
        }

        // If no swaps were made in this pass,
        // the array is sorted. We can stop early.
        if (swapped == 0) {
            break;
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

    bubbleSort(arr, len);

    printf("\nSorted Array:- ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 1;
}
