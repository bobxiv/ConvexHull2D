#include <cstdlib>
#include <ctime>

#include "App.h"

int main(int argc, char* argv[])
{
	srand((unsigned int)time(NULL));//ponemos una semilla pseudo-aleatoria

	App MyApp;//El objeto de aplicacion principal

	MyApp.Iniciar();

	return 0;
}

