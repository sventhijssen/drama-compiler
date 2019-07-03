int a;
main() {
	a = getint();
	while (a != 0) {
		if (a < 0)
			a = -a;
		printint (a);
		a = getint();
	}
}