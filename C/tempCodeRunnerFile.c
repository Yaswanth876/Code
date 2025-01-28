#include <stdio.h>

void selectionSortRecursive(int arr[], int n, int i) {
    if (i == n - 1) {
        return; // Base case: If we reached the last element
    }

    int minIndex = i;
    for (int j = i + 1; j < n; j++) {
        if (arr[j] < arr[minIndex]) {
            minIndex = j;
        }
    }

    // Swap the found minimum element with the first element
    int temp = arr[minIndex];
    arr[minIndex] = arr[i];
    arr[i] = temp;

    // Recursively sort the remaining array
    selectionSortRecursive(arr, n, i + 1);
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);

    selectionSortRecursive(arr, n, 0);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
