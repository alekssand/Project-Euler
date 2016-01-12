#include <stdio.h>
#include <stdint.h>

uint64_t comb(int n, int r);

int main()
{
        uint64_t count = 1;

        for( int k = 1 ; ; k++ )
        {
                int n = 2*k+1;
                int r = 50-4*k+1;
                if( r < 0 ) break;
                count += comb(n+r-1, r);
        }
        printf("Answer = %ju\n", count);
}

uint64_t comb(int n, int r)
{
        uint64_t c = 1;
        if( 2*r > n ) r = n-r;
        for( int i = 1 ; i <= r ; i++ )
        {
                c *= n--;
                c /= i;
        }
        return c;
}