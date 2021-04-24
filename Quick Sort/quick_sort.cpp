void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        //partition the array
        int pivot = partition(arr, low, high);

        //recursion process sub arrays
        quickSort(arr, low, pivot);
        quickSort(arr, pivot + 1, high);
    }
}