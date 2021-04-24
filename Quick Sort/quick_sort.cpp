#include <iostream>
using namespace std;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

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

    // put pivot in place
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
    for (int i=0; i < size; i++)
        cout<<arr[i]<<"\t";
}

int main()
{
    int arr[] = {87,82,40,89,34,76,44,96,54,20,79,65};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout<<"Input"<<endl;
    printArray(arr,n);
    cout<<endl;

    quickSort(arr, 0, n-1);
    cout<<"Output"<<endl;
    printArray(arr,n);
    return 100;
}
