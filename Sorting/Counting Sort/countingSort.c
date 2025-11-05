#include <stdio.h>
#include <stdlib.h>

void countingSort(int* arr, int len) {
    int *countArr = (int *)malloc(10 * sizeof(int));
    
    for (int i = 0; i < len; i++) {
        int value = arr[i];

        if (countArr[value]) {
            countArr[value]++;
        } else {
            countArr[value] = 1;
        }
    } // O(N)

    int i = 0;
    for (int j = 0; j < 10; j++) {
        int count = countArr[j];
        printf("count %d %d", j, count);

        if (count) {
            for (int k = 0; k < count; k++) {
                arr[i] = j;
                i++;
            }// O(10)
        }
    } // O(10)

    /**
     * O(N) + O(10^2) = O(N)
     */
}

int main() {
    /**
     * Expecting A Fix Number Between 0 to 9; To Get O(N) Response.
     */

    int *arr = NULL, len;

    printf("Enter Count of Elements in an Array:- ");
    scanf("%d", &len);

    arr = (int *)malloc(len * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        exit(1); // Exit the Program on Allocation Failure
    }

    printf("Note: Element Should Between 0 to 9.\n");

    for (int i = 0; i < len; i++) {
        printf("Enter Elements at %d:- ", i + 1);
        scanf("%d", &arr[i]);

        if (arr[i] < 0 || arr[i] > 9) {
            printf("Invalid Input: Element Should Between 0 to 9.\n");
            i--;
        }
    }

    countingSort(arr, len);

    printf("\nSorted Array:- ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 1;
}
