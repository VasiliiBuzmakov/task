#include "testlib.h"

int main(int argc, char* argv[]) {
    registerValidation(argc, argv);
    int n = inf.readInt(1, 100000, "N");
    inf.readSpace();
    int k = inf.readInt(1, n, "K");
    inf.readEoln();
    for (size_t i = 0; i < n; i++) {
        inf.readInt(1, 1000000, "a_i");
        if (i < n - 1) {
            inf.readSpace();
        }
    }
    inf.readEoln();
    inf.readEof();
}
