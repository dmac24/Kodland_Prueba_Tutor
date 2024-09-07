# Kodland_Prueba_Tutor

## Descripción
Para esta prueba se hizo una versión a Color del Trex Corredor de Google, el minijuego, que oficialmente es llamado “Chrome Dino” y que aparece cuando el navegador no puede conectarse a Internet. <br>
En esta versión del juego, se reproduce con personajes a color y sin mensajes de erroresd de conexión. <br>
Es divertido y el jugador controla al dinosaurio que debe saltar sobre obstáculos. El objetivo es ver cuánto tiempo puedes correr sin chocar.<br>


## Tecnologías
- ![Python](https://img.shields.io/badge/-Python-7F5AB6?logo=Python&style=flat-square&labelColor=282828)
- ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=GitHub&style=flat-square&labelColor=282828)
- ![Pygame ](https://img.shields.io/badge/-Pygame-7F5AB6?logo=Python&style=flat-square&labelColor=282828)


## Instalación
1. Clona este repositorio:
```bash
    git clone https://github.com/dmac24/Kodland_Prueba_Tutor
```
2. Navega a la carpeta del proyecto:
 ```bash
    cd Kodland_Prueba_Tutor
  ```
3. Instala Pygame:
 ```bash
    pip install pygame
 ```

## Uso
Para ejecutar el juego, simplemente usa:
```bash
python main.py
```

## Estructura del Proyecto 
```bash
├── main.py                
├── juego/                  # Lógica del juego
│   ├── __init__.py
│   ├── jugador.py          # Manejo de Jugador
│   ├── obstaculo.py        # Obstáculos
│   ├── estado.py           # Estados del Juego
├── recursos/               # Recursos (imágenes, sonidos)
│   ├── backgroundImg.png
│   ├── gameOver.png
│   ├── ground.png
│   ├── restart.png
│   ├── jugador/
│   │   ├── trex_1.png
│   │   ├── trex_2.png
│   │   └── trex_3.png
│   ├── obstaculos/
│   │   ├── obstaculo1.png
│   │   ├── obstaculo2.png
│   │   ├── obstaculo3.png
│   │   └── obstaculo4.png
│   ├── sonidos/
│   │   ├── jump.wav
│   │   └── collided.wav
│── Estructura.txt
└── README.md               # Documentación
```