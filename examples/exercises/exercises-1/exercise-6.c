int a, b, prod, aantal;

main() {
    aantal = getint();
    a = 1;
    while (a <= aantal) {
        b = 1;
        while (b <= aantal) {
            prod = a * b;
            printint (a, b, prod);
            b += 1;
        }
        a += 1;
    }
}