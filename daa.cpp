#include <iostream>
using namespace std;
int main() {
    int n,arr[100],target;
    cout << "enter the number of elements: ";
    cin >> n;
    cout << "enter the target element: ";
    cin >> target;
    for (int i = 0; i < n; i++)
    {
        cout << "enter the element: ";
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            cout << "element found at index: " << i << endl;
            break;
        }
    }
    
    return 0;
}