register int v;
int w;
int x = 0;
int y = 5;
int z[] = {1, 2, 3};
void a() {
	int i, j;
	register int k;
	i = k;
}
void b() {
	int r[10];
	a();
}
main() {
	a( );
	b( );
}
