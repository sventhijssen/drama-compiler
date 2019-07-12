int a[10] = {1,2,3,4,5,6,7,8,9,10};
register int som, i;
main()
{
	som = 0;
	i = 0;
	while (10 > i) {
		som += a[i];
		i++;
	}
	printint (som);
}
