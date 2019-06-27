struct Tschakelaar {
	int lokaal;
	int nr;
	int aan;
};

struct Tschakelaar s1, s2;

main()
{
	s1.lokaal = getint();
	s1.nr = getint();
	s1.aan = 1;
	s2 = s1;
}
