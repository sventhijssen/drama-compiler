int getal, aantal;

main() {
    aantal = 0;
    getal = getint();
    while (getal >= 0) {
        aantal = aantal + 1;
        getal = getint();
    }
    printint(aantal);
}