#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 7;
const int DELTA = 2;
const vector<int> prev_a = { 11, 18, 19, 20, 22, 25 };

bool next_mask(vector<int>& mask, int base) 
{
    int carry = 1;
    for(int i = 0; carry != 0 && i < N; ++i) 
    {
        mask[i] += carry;
        carry = mask[i] == base;
        if(carry) 
            mask[i] = 0;
    }
    return carry == 0;
}

int* special_sum(vector<int> a) 
{
    static const int B = 1;
    static const int C = 2;
    int sum[3];
    vector<int> mask(N);
    while(next_mask(mask, 3)) 
    {
        sum[0] = sum[1] = sum[2] = 0;
        int size[] = { 0, 0, 0};
        for(int i = 0; i < N; ++i) 
        {
            ++size[mask[i]];
            sum[mask[i]] += a[i];
        }
        if(size[B] != 0 && size[C] != 0 && (sum[B] == sum[C] || (size[B] != size[C] && size[B] > size[C] != sum[B] > sum[C]))) 
            return nullptr;
    }
    return new int(sum[0] + sum[1] + sum[2]);
}

int main() 
{
    vector<int> a(N);
    a[0] = prev_a[(N - 1) / 2];
    for(int i = 1; i < N; ++i) 
    {
        a[i] = a[0] + prev_a[i - 1];
    }
    int best_sum = 1e9;
    auto best_a = a;
    for(vector<int> mask(N);;) 
    {
        auto b = a;
        for(int i = 0; i < N; ++i) 
        {
            b[i] += mask[i] - DELTA;
        }
        auto sum = special_sum(b);
        if(sum != nullptr) 
        {
            if(*sum < best_sum) 
            {
                cout << *sum << " { ";
                sort(b.begin(), b.end());
                for(int i = 0; i < N; ++i) 
                {
                    cout << b[i] << (i == N - 1 ? " " : ", ");
                }
                cout << "}\n";
                best_sum = *sum;
                best_a = b;
            }
        }
        if(!next_mask(mask, 2 * DELTA + 1)) 
            break;
    }
    for(int i = 0; i < N; ++i) 
        cout << best_a[i];
    
    cout << endl;
    return 0;
}