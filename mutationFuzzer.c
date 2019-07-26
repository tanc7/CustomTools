#include <stdio.h>
#include <stdlib.h>

void SimpleFuzzer(const char* data, size_t length) {
    size_t position = RandomInt(length);
    size_t bit = RandomInt(8);
    char* copy = CopyData(data, length);
    copy[position] ^= (1 << bit);
    SendData(copy, length);
}