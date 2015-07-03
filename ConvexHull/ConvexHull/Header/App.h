#pragma once

#include "SFML//Graphics.hpp"
#include "SFML//System.hpp"
#include "SFML//Window.hpp"
#include "SFML//Config.hpp"

#include "ConvexHull2D.h"

//Clase principal del juego, contiene toda la estructura de juego
//Este objeto sera el responsable de:
//	-Crear la escena
//	-Dibujar la pantalla
//	-Actualizar el juego
class App
{
private:
	
	//Ventana principal
	sf::RenderWindow m_Window;

	sf::Event        m_Evento;

	//Elementos de la escena:
	//-----------------------
	ConvexHull2D*    m_pCascoConvexo;
	std::vector<Vertex2D> m_P;

public:

	App();

	~App();

	//Inicializa la escena, se llama luego de creada la instacia de App
	void Iniciar();

	//Crea la escena
	void CrearEscena();

	//Actualiza la escena
	void Actualizar();

	//Dibuja la escena
	void Dibujar();

};