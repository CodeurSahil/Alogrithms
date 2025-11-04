#include <stdio.h>
#include <stdlib.h>

void merge (int* arr, int startIndex, int mid, int endIndex) {
    int sizeOfArr1 = mid - startIndex + 1;
    int sizeOfArr2 = endIndex - mid;

    int * tmpArr1 = (int *)malloc(sizeOfArr1 * sizeof(int));
    int * tmpArr2 = (int *)malloc(sizeOfArr2 * sizeof(int));

    for (int i = 0; i < sizeOfArr1; i++) {
        tmpArr1[i] = arr[startIndex + i];
    }

    for (int j = 0; j < sizeOfArr2; j++) {
        tmpArr2[j] = arr[mid + 1 + j];
    }

    int i = 0, j = 0, k = startIndex;

    while (i < sizeOfArr1 && j < sizeOfArr2) {
        if (tmpArr1[i] <= tmpArr2[j]){
            arr[k] = tmpArr1[i];
            i++;
        } else {
            arr[k] = tmpArr2[j];
            j++;
        }
        k++;
    }

    while (i < sizeOfArr1) {
        arr[k] = tmpArr1[i];
        i++;
        k++;
    }

    while (j < sizeOfArr2) {
        arr[k] = tmpArr2[j];
        j++;
        k++;
    }  
    
    free(tmpArr1);
    free(tmpArr2);
}

void mergeSort(int* arr, int startIndex, int endIndex) {
    if (endIndex - startIndex + 1 <= 1) {
        return;
    }
    
    int mid = startIndex + (endIndex - startIndex) / 2;

    mergeSort(arr, startIndex, mid);
    mergeSort(arr, mid + 1, endIndex);

    merge(arr, startIndex, mid, endIndex);
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

    mergeSort(arr, 0, len - 1);

    printf("\nSorted Array:- ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);

    return 1;
}
