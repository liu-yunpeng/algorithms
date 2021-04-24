// use the first element as pivot
int partition (int arr[], int low, int high)
{
    int pivot = arr[low];
    int i = low;

    for (int j = low + 1; j <= high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i], &arr[low]);
    return (i);
}


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



void printArray(int arr[], int size)
{
    
}