int getal, aantal, apos, aneg, anul, n;

main() {
    anul = apos = aneg = aantal = 0;
    n = getint();
    while (aantal < n) {
        getal = getint();
        aantal = aantal + 1;
        if (getal == 0)
            anul += 1;
        else if (getal > 0)
            apos += 1;
        else
            aneg += 1;
    }
    printint(anul, apos, aneg);
}