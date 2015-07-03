#include <cstdlib>

#include "App.h"

//-------------------------------------------------------------//
//-------------	Constructor/Destructor	-----------------------//
//-------------------------------------------------------------//

App::App(): m_Window(sf::VideoMode(800,600,32), "Casco Convexo 2D"), m_pCascoConvexo(NULL)
{
	m_Window.Show(true);
	m_Window.SetFramerateLimit(60);

	CrearEscena();
}

App::~App()
{
	if( m_pCascoConvexo )
		delete m_pCascoConvexo;
}

//-------------------------------------------------------------//
//-----------------		Metodos		---------------------------//
//-------------------------------------------------------------//

void App::CrearEscena()
{
	if( m_pCascoConvexo )
		delete m_pCascoConvexo;

	m_P.clear();

	for(int k=0; k < 200 ; ++k)
		m_P.push_back(Vertex2D((rand()/(float)RAND_MAX)*800,(rand()/(float)RAND_MAX)*600));

	m_pCascoConvexo = new ConvexHull2D(m_P, ConvexHull2D::Graham);
}

void App::Iniciar()
{
	const sf::Input& input = m_Window.GetInput();

	while( m_Window.IsOpened() )
	{
		//Atrapamos los eventos para cerra la ventana y los clicks del mouse
		while( m_Window.GetEvent(m_Evento) )
		{
			switch( m_Evento.Type )
			{
			case sf::Event::Closed:
					m_Window.Close();
				break;
				
			case sf::Event::KeyPressed:
				if( m_Evento.Key.Code == sf::Key::Escape)
					m_Window.Close();
				if( m_Evento.Key.Code == sf::Key::R )
					CrearEscena();
				break;

			case sf::Event::MouseButtonPressed:
				{
					Vertex2D Punto((float)m_Evento.MouseButton.X, (float)m_Evento.MouseButton.Y);
				}
				break;

			case sf::Event::MouseLeft:
			case sf::Event::MouseButtonReleased:
				break;

			case sf::Event::MouseMoved:
				break;
			}
		}

		Actualizar();    //Actualizamos la escena

		Dibujar();       //Dibujamos toda la escena
	}
}

void App::Actualizar()
{
}

void App::Dibujar()
{
	m_Window.Clear();

	m_pCascoConvexo->Dibujar(m_Window);

	sf::Shape circle;
	for(int v=0; v < m_P.size() ; ++v)
	{
		circle = sf::Shape::Circle(sf::Vector2f(m_P[v].x, m_P[v].y), 3.0f, sf::Color::Red);
		m_Window.Draw(circle);
	}

	m_Window.Display();
}