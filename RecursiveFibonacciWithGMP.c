/* For counting large Fibonacci numbers recursively without variable type limitations, 
only available memory by using GMP. */

#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void recursiveFibonacci(mpz_t n, mpz_t n2, int i, int t){
	if(i < t){
		mpz_add(n,n,n2);
		recursiveFibonacci(n2, n, ++i, t);
	}
}

int main(int argc, char *argv[]){
	int t;
	
	/* Init mpz variables*/
	mpz_t n;
	mpz_t n2;

	mpz_init(n);
	mpz_init(n2);

	mpz_set_ui(n, 0);
	mpz_set_ui(n2, 1);
	
	if(argc == 1){
		printf("Anna luku, jolle lasketaan Fibonaccin luku: ");
		scanf("%d", &t);
	}else if(argc == 2){
		t = atoi(argv[1]);
	}else{
		printf("Wrong amount of arguments.");
		exit(1);
	}

	if(t < 1){
		printf("Luvun pitää olla suurempi kuin 0.\n");
		exit(1);	
	}

	recursiveFibonacci(n,n2,1,t);

	gmp_printf("Luvun %d Fibonacci luku on %Zd.\n",t, n);
	
	/* Free the memory*/
	mpz_clear(n);
	mpz_clear(n2);

	return(0);
}
