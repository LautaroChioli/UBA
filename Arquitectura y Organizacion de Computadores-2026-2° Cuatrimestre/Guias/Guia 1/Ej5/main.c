#include <stdio.h>



int main() {
    float fn = 0.1;
    printf("float: %f\n", fn);
    double dn = 0.51;
    printf("double: %f\n", dn);

    int castedfn = (int) fn;
    printf("casted float: %d\n", castedfn);
    int casteddn = (int) dn;
    printf("casted double: %d\n", casteddn);

}