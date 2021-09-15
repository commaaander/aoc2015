#include <stdio.h>

#define P  33100000  // puzzle input
#define N   1000000  // number of houses (arbitrary)
#define M1       10  // elf multiplier (part 1)
#define M2       11  // elf multiplier (part 2)
#define LIM      50  // max house visits (part 2)

int presents[N] = {M1};  // init for part 1

int main(void)
{
    int elf, house, pres, visit;

    // Part 1: distribute presents (elf 1 already visited by init)
    for (elf = 2; elf < N; ++elf) {
        pres = elf * M1;
        for (house = elf; house < N; house += elf) {
            presents[house] += pres;
        }
    }

    // Part 1: find lowest house number where number of presents >= puzzle input
    for (house = 1; house < N; ++house) {
        if (presents[house] >= P) {
            printf("Part 1: %d\n", house);
            break;
        }
    }

    // Part 2: reset
    for (house = 1; house < N; ++house) {
        presents[house] = M2;
    }

    // Part 2: distribute presents
    // Elf 1 already visited by reset
    for (elf = 2; elf < N; ++elf) {
        pres = elf * M2;
        visit = 0;
        for (house = elf; visit++ < LIM && house < N; house += elf) {
            presents[house] += pres;
        }
    }

    // Part 2: find lowest house number where number of presents >= puzzle input
    for (house = 1; house < N; ++house) {
        if (presents[house] >= P) {
            printf("Part 2: %d\n", house);
            break;
        }
    }

    return 0;
}
