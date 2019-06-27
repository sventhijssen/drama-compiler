int rij[10];
int getal;
int aantal;
main()
{
    aantal = 0;
    getal = getint();
    while (getal >= 0)
    {
        aantal = aantal + 1;
        getal = getint();
    }
printint(aantal);
}