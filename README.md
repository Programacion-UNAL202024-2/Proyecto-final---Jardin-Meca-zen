# 🌱 Tamagotchi_Zen
## 👥 Aqui estaran los integrantes de un juego sencillo pero funcional :

##### -*Manuel Federico Castro Suárez*
##### -*Gabriel Felipe Garzón Rosero*
##### -*Franklin Orlando Delgado Ramirez*
##### -*Jhorsmith Pena Perez*

## 📜 Resumen
**Tamagotchi_Zen** es un juego de simulación en el que el jugador debe cuidar de una planta virtual. 🌿 El objetivo es mantener la planta viva y hacerla crecer a través de diferentes fases, superando eventos aleatorios como sequías, lluvias y tormentas. 🌧️🌪️ El jugador debe administrar los recursos de agua 💧 y abono 🌱 para asegurar que la planta sobreviva y florezca. 🌸

## 🎯 Objetivos
- **Cuidar la planta**: 🌿 Mantener la planta viva administrando los recursos de agua 💧 y abono 🌱.
- **Superar fases**: 🚀 Avanzar a través de 3 fases de crecimiento, cumpliendo con los requisitos de agua 💧 y abono 🌱 en cada una.
- **Sobrevivir a eventos**: 🌪️ Manejar eventos aleatorios que afectan los recursos de la planta.
- **Ganar el juego**: 🏆 Alcanzar la fase 3 con suficientes recursos antes de que se agote el tiempo ⏳.

## 🌟 Características Principales
- **Interacción con la planta**: 🖱️ El jugador puede arrastrar agua 💧 y abono 🌱 hacia la planta para mantenerla viva.
- **Eventos aleatorios**: 🌧️ Sequías, lluvias y tormentas 🌪️ afectan los recursos de la planta.
- **Fases de crecimiento**: 🌱 La planta avanza a través de 3 fases, cada una con requisitos más difíciles.
- **Pantallas de inicio, ganar y perder**: 🖼️ Interfaz gráfica con fondos personalizados y texto con contorno para mejorar la legibilidad.
- **Música y efectos de sonido**: 🎶 Ambiente sonoro que mejora la experiencia del jugador.

## 💻 Lenguajes y Tecnologías
- **Lenguaje de programación**: 🐍 Python
- **Bibliotecas principales**:
  - 🎮 `pygame`: Para la creación de la interfaz gráfica y la gestión de eventos.
  - 🎲 `random`: Para la generación de eventos aleatorios.
  - ⏱️ `time`: Para la gestión del tiempo en el juego.

## 🛠️ Temas de Programación Usados
- **Estructuras condicionales**: Uso de `if`, `elif` y `else` para manejar decisiones en el juego, como verificar si la planta está viva o si se cumplen los requisitos para avanzar de fase.
- **Bucles**: Uso de `while` para el bucle principal del juego y `for` para iterar sobre listas o dibujar elementos como la lluvia o los eventos especiales.
- **Funciones**: Creación y uso de funciones para modularizar el código, como `dibujar_plantita()`, `aplicar_evento_efectos()` y `mostrar_pantalla_inicio()`.
- **Manejo de eventos**: Uso de estructuras como `pygame.event.get()` para gestionar eventos del usuario, como clics del ratón y movimientos.
- **Listas y diccionarios**: Uso de listas para almacenar instrucciones o eventos, y diccionarios para manejar el estado de la planta (`plantita`).
- **Colisiones**: Detección de colisiones entre el cursor y la planta usando `collidepoint()`.
- **Manejo del tiempo**: Uso de `time.time()` para gestionar el tiempo restante, los eventos y el decremento de recursos.
- **Dibujo y animaciones**: Uso de `pygame.draw` y `pygame.blit` para dibujar elementos en la pantalla, como la planta, los botones y los eventos meteorológicos.
- **Manejo de recursos**: Uso de variables globales para gestionar el agua, el abono y el tiempo restante.

## 🕹️ Instrucciones de Uso
1. **Iniciar el juego**: 🚀 Ejecuta el archivo `main.py` para comenzar.
2. **Menú principal**: 🏠 Haz clic en "Jugar" para comenzar el juego.
3. **Cuidar la planta**: 🌿 Arrastra los iconos de agua 💧 y abono 🌱 hacia la planta para mantenerla viva.
4. **Superar fases**: 🚀 Cumple con los requisitos de agua 💧 y abono 🌱 para avanzar a la siguiente fase.
5. **Manejar eventos**: 🌧️🌪️ Sobrevive a los eventos aleatorios que afectan los recursos de la planta.
6. **Ganar el juego**: 🏆 Alcanza la fase 3 con suficientes recursos antes de que se agote el tiempo ⏳.

## ⚙️ Requisitos del Sistema
- 🐍 Python 3.x instalado.
- 🎮 Biblioteca `pygame` instalada. Puedes instalarla con el siguiente comando:
  ```bash
  pip install pygame

## Diagrama de Flujo
<div align ="center>
  <img src="https://github.com/Programacion-UNAL202024-2/Proyecto-final--TamagotchiZen/blob/main/assets/diagrama.png" alt="Aquí hay un diagrama de flujo" width="1000px">
</div>

## 🌷 Capturas
<div align="center">
  <img src="ttps://github.com/Programacion-UNAL202024-2/Proyecto-final--TamagotchiZen/blob/283013a10776bbaa14f643318885fbd192e7a330/assets/diagrama.png" alt="xd" width="800px">
</div>

<div align="center">
  <img src="https://github.com/Programacion-UNAL202024-2/Proyecto-final--TamagotchiZen/blob/main/assets/captura_juego_desierto.jpeg" alt="xd" width="800px">
</div>
