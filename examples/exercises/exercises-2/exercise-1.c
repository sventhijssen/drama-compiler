int f[100], i, n;

main() {
    n = getint();
    f[0] = 1;
    f[1] = 1;
    printint (f[0], f[1]);
    i = 2;
    while (i < n) {
        f[i] = f[i-1] + f[i-2];
        printint(f[i++]);
    }
}