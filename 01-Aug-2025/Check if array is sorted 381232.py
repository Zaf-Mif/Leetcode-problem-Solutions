# Problem: Check if array is sorted - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

#include <stdbool.h>  // For using bool, true, false

bool isSorted(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            return false; // Found a decreasing pair
        }
    }
    return true; // All elements were in order
}
