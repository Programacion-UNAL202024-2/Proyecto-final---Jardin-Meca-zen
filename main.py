import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tamagotchi_Zen")

# Cargar música de fondo
pygame.mixer.music.load("assets/musica_fondo.mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle

# Cargar efectos de sonido
sonido_agua = pygame.mixer.Sound("assets/agua.mp3")
sonido_abono = pygame.mixer.Sound("assets/abono.mp3")

# Cargar imágenes (alto, ancho)
plantita_imagen = pygame.image.load("assets/plantita.png")
plantita_imagen = pygame.transform.scale(plantita_imagen, (100, 100))

plantita_fase1 = pygame.image.load("assets/plantita_fase1.png")
plantita_fase1 = pygame.transform.scale(plantita_fase1, (90, 90))

plantita_fase2 = pygame.image.load("assets/plantita_fase2.png")
plantita_fase2 = pygame.transform.scale(plantita_fase2, (78, 135))

plantita_fase3 = pygame.image.load("assets/plantita_fase3.png")  
plantita_fase3 = pygame.transform.scale(plantita_fase3, (80, 130))

regadera_imagen = pygame.image.load("assets/agua_cursor.png")
regadera_imagen = pygame.transform.scale(regadera_imagen, (60, 60))

abono_imagen = pygame.image.load("assets/abono_cursor.png")
abono_imagen = pygame.transform.scale(abono_imagen, (60, 60))

fondo_principal = pygame.image.load("assets/fondo_principal.jpg")
fondo_principal = pygame.transform.scale(fondo_principal, (600, 400))

fondo_ganar = pygame.image.load("assets/fondo_ganar.jpeg")
fondo_ganar = pygame.transform.scale(fondo_ganar, (600, 400))

fondo_perder = pygame.image.load("assets/fondo_perder.jpeg")
fondo_perder = pygame.transform.scale(fondo_perder, (600, 400))

fondo_menu = pygame.image.load("assets/fondo_menu.jpeg")
fondo_menu = pygame.transform.scale(fondo_menu, (600, 400))

# Imágenes para eventos especiales
try:
    desierto_imagen = pygame.image.load("assets/desierto.jpg")
    desierto_imagen = pygame.transform.scale(desierto_imagen, (600, 400))

    lluvia_imagen = pygame.image.load("assets/lluvia.jpg")
    lluvia_imagen = pygame.transform.scale(lluvia_imagen, (600, 400))

    tormenta_imagen = pygame.image.load("assets/tormenta.jpg")
    tormenta_imagen = pygame.transform.scale(tormenta_imagen, (600, 400))
except pygame.error:
    # Si no se encuentran las imágenes, crear superficies de colores
    desierto_imagen = pygame.Surface((600, 400))
    desierto_imagen.fill((245, 222, 179))  # Color arena
    
    lluvia_imagen = pygame.Surface((600, 400))
    lluvia_imagen.fill((176, 196, 222))  # Color azul claro

    tormenta_imagen = pygame.Surface((600, 400))
    tormenta_imagen.fill((176, 196, 222)) # Color azul

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
VERDE_OSCURO = (0, 100, 0)
ROJO = (255, 0, 0)
GRIS = (200, 200, 200)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 255)
NARANJA = (255, 165, 0)

# Fuentes
fuente = pygame.font.Font(None, 36)
fuente_pequena = pygame.font.Font(None, 24)

# Estados del juego
plantita = {"fase": 0, "agua": 5, "abono": 5, "viva": True}
tiempo_restante = 80
tiempo_total = 80

# Eventos
evento_actual = None
tiempo_inicio_evento = 0
eventos = ["desierto", "lluvioso", "tormenta", None]

# Requisitos para crecer (aumentados para hacer el juego más largo)
requisitos_fase1 = {"agua": 8, "abono": 8}
requisitos_fase2 = {"agua": 10, "abono": 10}
requisitos_fase3 = {"agua": 16, "abono": 16}

# Avisos
aviso = None
tiempo_aviso = 0
duracion_aviso = 3  # Duración del aviso en segundos

# Botones
boton_agua_rect = pygame.Rect(50, 270, 60, 60)
boton_abono_rect = pygame.Rect(500, 270, 60, 60)
boton_play_rect = pygame.Rect(230, 270, 150, 50)

# Área de la plantita para detectar colisiones
plantita_rect = pygame.Rect(250, 150, 150, 150)

# Nivel de dificultad base (aumentará con cada fase)
nivel_dificultad = 1

# Variables de arrastre
arrastrando = False
objeto_arrastrado = None
posicion_arrastre = (0, 0)

# Variables de tiempo
tiempo_inicio_juego = 0
tiempo_ultimo_evento = 0
tiempo_ultimo_decremento = 0
tiempo_ultimo_aumento_dificultad = 0
intervalo_eventos = 15  # Cada 15 segundos puede ocurrir un evento
duracion_evento = 10  # Duración de cada evento en segundos
intervalo_aumento_dificultad = 20  # Aumenta la dificultad cada 20 segundos

# Función para reiniciar el juego
def reiniciar_juego():
    global plantita, tiempo_restante, evento_actual, nivel_dificultad, tiempo_inicio_juego
    global tiempo_ultimo_evento, tiempo_ultimo_decremento, tiempo_ultimo_aumento_dificultad
    
    plantita = {"fase": 0, "agua": 5, "abono": 5, "viva": True}
    tiempo_restante = 80
    evento_actual = None
    nivel_dificultad = 1
    
    # Reiniciar todos los tiempos
    tiempo_actual = time.time()
    tiempo_inicio_juego = tiempo_actual
    tiempo_ultimo_evento = tiempo_actual
    tiempo_ultimo_decremento = tiempo_actual
    tiempo_ultimo_aumento_dificultad = tiempo_actual

# Función para generar eventos aleatorios
def generar_evento():
    global evento_actual, tiempo_inicio_evento
    
    # Solo genera un evento si no hay uno activo
    if evento_actual is None:
        # Mayor probabilidad de evento con nivel de dificultad más alto
        probabilidad = 0.2 * nivel_dificultad
        if random.random() < probabilidad:
            # Más eventos dificiles en fases avanzadas
            if plantita["fase"] < 2:
                eventos_posibles = ["desierto", "lluvioso"]
            else:
                eventos_posibles = ["desierto", "lluvioso", "tormenta"]
                
            evento_actual = random.choice(eventos_posibles)
            tiempo_inicio_evento = time.time()
            return True
    return False

# Función para finalizar evento
def finalizar_evento():
    global evento_actual
    evento_actual = None

# Función para aplicar efectos de eventos
def aplicar_evento_efectos():
    global plantita, aviso, tiempo_aviso, tiempo_ultimo_decremento
    
    tiempo_actual = time.time()
    
    # Factor de dificultad aumenta con la fase
    factor_dificultad = nivel_dificultad * (0.5 + plantita["fase"] * 0.3)
    
    # Efectos de desierto: disminuye el agua más rápido
    if evento_actual == "desierto":
        if tiempo_actual - tiempo_ultimo_decremento > 1.5 / factor_dificultad:
            plantita["agua"] = max(0, plantita["agua"] - 1)
            if plantita["agua"] <= 2:
                aviso = "¡Necesitas agua urgente!"
                tiempo_aviso = tiempo_actual
            tiempo_ultimo_decremento = tiempo_actual
    
    # Efectos de lluvia: aumenta el agua pero disminuye el abono
    elif evento_actual == "lluvioso":
        if tiempo_actual - tiempo_ultimo_decremento > 2 / factor_dificultad:
            plantita["agua"] = min(20, plantita["agua"] + 0.7)
            plantita["abono"] = max(0, plantita["abono"] - 0.5)
            if plantita["abono"] <= 2:
                aviso = "¡Necesitas abono urgente!"
                tiempo_aviso = tiempo_actual
            tiempo_ultimo_decremento = tiempo_actual
            
    # Efectos de tormenta: disminuye tanto agua como abono (evento más dificil)
    elif evento_actual == "tormenta":
        if tiempo_actual - tiempo_ultimo_decremento > 1.2 / factor_dificultad:
            plantita["agua"] = max(0, plantita["agua"] - 0.07)
            plantita["abono"] = max(0, plantita["abono"] - 0.2)
            if plantita["agua"] <= 2 or plantita["abono"] <= 2:
                aviso = "¡La tormenta está dañando tu planta!"
                tiempo_aviso = tiempo_actual
            tiempo_ultimo_decremento = tiempo_actual

# Función para verificar si la planta sigue viva
def verificar_planta_viva():
    if plantita["agua"] <= 0 or plantita["abono"] <= 0:
        plantita["viva"] = False

# Función para decrementar recursos con el tiempo
def decrementar_recursos():
    global plantita, tiempo_ultimo_decremento, aviso, tiempo_aviso
    
    tiempo_actual = time.time()
    
    # Tasa de decremento aumenta con la fase y la dificultad
    factor_fase = 1 + (plantita["fase"] * 0.5)
    tasa_decremento = 3.0 * (1 + (nivel_dificultad - 1) * 0.3) / factor_fase
    
    if tiempo_actual - tiempo_ultimo_decremento > tasa_decremento:
        # Decremento más rápido en fases avanzadas
        decremento_base = 0.5 * (1 + plantita["fase"] * 0.2)
        
        plantita["agua"] = max(0, plantita["agua"] - decremento_base)
        plantita["abono"] = max(0, plantita["abono"] - decremento_base)
        
        # Generar avisos según los niveles
        if plantita["agua"] <= 2:
            aviso = "¡Necesitas agua!"
            tiempo_aviso = tiempo_actual
        elif plantita["abono"] <= 2:
            aviso = "¡Necesitas abono!"
            tiempo_aviso = tiempo_actual
            
        tiempo_ultimo_decremento = tiempo_actual

# Función para aumentar la dificultad con el tiempo
def aumentar_dificultad():
    global nivel_dificultad, tiempo_ultimo_aumento_dificultad
    
    tiempo_actual = time.time()
    if tiempo_actual - tiempo_ultimo_aumento_dificultad > intervalo_aumento_dificultad:
        nivel_dificultad = min(5, nivel_dificultad + 1)  # Máximo nivel 5
        tiempo_ultimo_aumento_dificultad = tiempo_actual

# Función para dibujar la plantita
def dibujar_plantita():
    global plantita_rect
    
    # Actualizar el área de colisión según la fase
    if plantita["fase"] == 0:
        pantalla.blit(plantita_imagen, (245, 200))
        plantita_rect = pygame.Rect(265, 200, 70, 100)
    elif plantita["fase"] == 1:
        pantalla.blit(plantita_fase1, (245, 200))
        plantita_rect = pygame.Rect(265, 200, 70, 100)
    elif plantita["fase"] == 2:
        pantalla.blit(plantita_fase2, (260, 180))
        plantita_rect = pygame.Rect(265, 200, 100, 120)
    elif plantita["fase"] == 3:
        pantalla.blit(plantita_fase3, (260, 180))
        plantita_rect = pygame.Rect(265, 200, 100, 120)

# Función para iniciar arrastre
def iniciar_arrastre(pos):
    global arrastrando, objeto_arrastrado, posicion_arrastre
    
    if boton_agua_rect.collidepoint(pos):
        arrastrando = True
        objeto_arrastrado = "agua"
        posicion_arrastre = pos
        # Ocultar el cursor durante el arrastre
        pygame.mouse.set_visible(False)
    elif boton_abono_rect.collidepoint(pos):
        arrastrando = True
        objeto_arrastrado = "abono"
        posicion_arrastre = pos
        # Ocultar el cursor durante el arrastre
        pygame.mouse.set_visible(False)

# Función para finalizar arrastre
def finalizar_arrastre(pos):
    global arrastrando, objeto_arrastrado, posicion_arrastre, plantita
    
    if arrastrando:
        # Verificar si se suelta encima de la plantita
        if plantita_rect.collidepoint(pos):
            if objeto_arrastrado == "agua" and plantita["agua"] < 20:
                # La efectividad disminuye con la fase
                aumento = 1.0 / (1 + plantita["fase"] * 0.25)
                plantita["agua"] = min(20, plantita["agua"] + aumento)
                sonido_agua.play()
            elif objeto_arrastrado == "abono" and plantita["abono"] < 20:
                # La efectividad disminuye con la fase
                aumento = 1.0 / (1 + plantita["fase"] * 0.25)
                plantita["abono"] = min(20, plantita["abono"] + aumento)
                sonido_abono.play()
        
        # Restaurar el cursor
        pygame.mouse.set_visible(True)
        arrastrando = False
        objeto_arrastrado = None

# Función para actualizar posición durante arrastre
def actualizar_arrastre(pos):
    global posicion_arrastre
    
    if arrastrando:
        posicion_arrastre = pos

# Función para dibujar objeto arrastrado
def dibujar_arrastre():
    if arrastrando:
        if objeto_arrastrado == "agua":
            # Ajustar posición para centrar en el cursor
            pantalla.blit(regadera_imagen, (posicion_arrastre[0] - 25, posicion_arrastre[1] - 25))
        elif objeto_arrastrado == "abono":
            # Ajustar posición para centrar en el cursor
            pantalla.blit(abono_imagen, (posicion_arrastre[0] - 25, posicion_arrastre[1] - 25))

# Función para actualizar la fase de la plantita
def actualizar_fase_plantita():
    if plantita["agua"] >= requisitos_fase1["agua"] and plantita["abono"] >= requisitos_fase1["abono"] and plantita["fase"] == 0:
        plantita["fase"] = 1
        mostrar_mensaje_fase("¡Fase 1 completada! La planta está creciendo.", 3)
    elif plantita["agua"] >= requisitos_fase2["agua"] and plantita["abono"] >= requisitos_fase2["abono"] and plantita["fase"] == 1:
        plantita["fase"] = 2
        mostrar_mensaje_fase("¡Fase 2 completada! La planta se fortalece.", 3)
    elif plantita["agua"] >= requisitos_fase3["agua"] and plantita["abono"] >= requisitos_fase3["abono"] and plantita["fase"] == 2:
        plantita["fase"] = 3
        mostrar_mensaje_fase("¡Fase 3 completada! La planta está floreciendo.", 3)
    elif plantita["fase"] == 3 and plantita["agua"] >= 18 and plantita["abono"] >= 18:
        # Victoria
        return True
    return False

# Función para mostrar mensajes de fase
def mostrar_mensaje_fase(mensaje, duracion):
    global aviso, tiempo_aviso
    
    aviso = mensaje
    tiempo_aviso = time.time()

# Función para dibujar eventos meteorológicos
def dibujar_lluvia():
    for _ in range(50):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        pygame.draw.line(pantalla, AZUL, (x, y), (x, y + 10), 2)

def dibujar_desierto():
    for _ in range(20):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        pygame.draw.circle(pantalla, (245, 222, 179), (x, y), 3)

def dibujar_tormenta():
    for _ in range(30):
        x = random.randint(0, ANCHO)
        y = random.randint(0, ALTO)
        pygame.draw.line(pantalla, AZUL, (x, y), (x + random.randint(-10, 10), y + 15), 3)
    
    # Rayos ocasionales
    if random.random() < 0.1:
        inicio_x = random.randint(100, ANCHO - 100)
        pygame.draw.line(pantalla, AMARILLO, (inicio_x, 0), (inicio_x + random.randint(-50, 50), 100), 4)

# Pantalla de "GAME OVER"
def mostrar_pantalla_perdido():
    pantalla.blit(fondo_perder, (0, 0))
    texto = fuente.render("¡Perdiste! La plantita murió.", True, BLANCO)
    pantalla.blit(texto, (150, 150))
    
    # Mostrar razón y fase alcanzada
    razon = ""
    if plantita["agua"] <= 0:
        razon = "Se secó por falta de agua."
    elif plantita["abono"] <= 0:
        razon = "Le faltaron nutrientes."
    
    texto_razon = fuente_pequena.render(razon, True, BLANCO)
    pantalla.blit(texto_razon, (200, 190))
    
    texto_fase = fuente_pequena.render(f"Llegaste hasta la fase {plantita['fase']}", True, BLANCO)
    pantalla.blit(texto_fase, (200, 220))
    
    pygame.draw.rect(pantalla, BLANCO, boton_play_rect)
    texto_play = fuente.render("Reintentar", True, NEGRO)
    pantalla.blit(texto_play, (250, 280))

# Pantalla de "Inicio"
def mostrar_pantalla_inicio():
    pantalla.blit(fondo_menu, (0, 0))
    texto_titulo = fuente.render("Tamagotchi - Cuida tu plantita", True, NEGRO)
    pantalla.blit(texto_titulo, (120, 100))
    
    # Instrucciones
    instrucciones = [
        "Ayuda a crecer tu planta dándole agua y abono.",
        "Arrastra los iconos y suéltalos sobre la planta.",
        "Pasa por 4 fases de crecimiento para ganar.",
        "Cada fase es más difícil que la anterior.",
        "Sobrevive a eventos especiales como sequías o tormentas."
    ]
    
    y_pos = 140
    for instruccion in instrucciones:
        texto_inst = fuente_pequena.render(instruccion, True, NEGRO)
        pantalla.blit(texto_inst, (100, y_pos))
        y_pos += 25
    
    pygame.draw.rect(pantalla, VERDE, boton_play_rect)
    texto_play = fuente.render("Jugar", True, NEGRO)
    pantalla.blit(texto_play, (270, 280))

# Pantalla de "Ganaste"
def mostrar_pantalla_ganar():
    pantalla.blit(fondo_ganar, (0, 0))
    texto = fuente.render("¡Felicidades! Has cultivado la planta perfecta.", True, NEGRO)
    pantalla.blit(texto, (30, 120))
    
    texto_tiempo = fuente_pequena.render(f"Tiempo restante: {int(tiempo_restante)} segundos", True, NEGRO)
    pantalla.blit(texto_tiempo, (200, 170))
    
    texto_dificultad = fuente_pequena.render(f"Nivel de dificultad alcanzado: {nivel_dificultad}", True, NEGRO)
    pantalla.blit(texto_dificultad, (170, 200))
    
    pygame.draw.rect(pantalla, BLANCO, boton_play_rect)
    texto_play = fuente.render("Reiniciar", True, NEGRO)
    pantalla.blit(texto_play, (250, 280))

# Función para dibujar barras de estado
def dibujar_barras_estado():
    # Barra de agua
    pygame.draw.rect(pantalla, NEGRO, (50, 50, 120, 20), 1)
    pygame.draw.rect(pantalla, AZUL, (51, 51, max(0, int(118 * plantita["agua"] / 20)), 18))
    texto_agua = fuente_pequena.render(f"Agua: {plantita['agua']:.1f}/20", True, NEGRO)
    pantalla.blit(texto_agua, (65, 30))
    
    # Barra de abono
    pygame.draw.rect(pantalla, NEGRO, (430, 50, 120, 20), 1)
    pygame.draw.rect(pantalla, VERDE, (431, 51, max(0, int(118 * plantita["abono"] / 20)), 18))
    texto_abono = fuente_pequena.render(f"Abono: {plantita['abono']:.1f}/20", True, NEGRO)
    pantalla.blit(texto_abono, (445, 30))
    
    # Barra de tiempo
    pygame.draw.rect(pantalla, NEGRO, (200, 20, 200, 15), 1)
    pygame.draw.rect(pantalla, AMARILLO, (201, 21, max(0, int(198 * tiempo_restante / tiempo_total)), 13))
    texto_tiempo = fuente_pequena.render(f"Tiempo: {int(tiempo_restante)}", True, NEGRO)
    pantalla.blit(texto_tiempo, (250, 40))
    
    # Nivel de dificultad y fase
    texto_nivel = fuente_pequena.render(f"Nivel: {nivel_dificultad}", True, NEGRO)
    pantalla.blit(texto_nivel, (20, 10))
    
    texto_fase = fuente_pequena.render(f"Fase: {plantita['fase']}/3", True, NEGRO)
    pantalla.blit(texto_fase, (20, 80))
    
    # Requisitos para avanzar a la siguiente fase
    if plantita["fase"] == 0:
        req_texto = f"Requisitos para fase 1: Agua {requisitos_fase1['agua']}, Abono {requisitos_fase1['abono']}"
    elif plantita["fase"] == 1:
        req_texto = f"Requisitos para fase 2: Agua {requisitos_fase2['agua']}, Abono {requisitos_fase2['abono']}"
    elif plantita["fase"] == 2:
        req_texto = f"Requisitos para fase 3: Agua {requisitos_fase3['agua']}, Abono {requisitos_fase3['abono']}"
    else:
        req_texto = "Requisitos para ganar: Agua 18, Abono 18"
    
    texto_req = fuente_pequena.render(req_texto, True, NEGRO)
    pantalla.blit(texto_req, (150, 80))

# Función para mostrar eventos especiales
def mostrar_evento():
    if evento_actual == "desierto":
        pantalla.blit(desierto_imagen, (0, 0))
        dibujar_desierto()
        texto_evento = fuente.render("¡SEQUÍA!", True, ROJO)
        pantalla.blit(texto_evento, (250, 100))
    elif evento_actual == "lluvioso":
        pantalla.blit(lluvia_imagen, (0, 0))
        dibujar_lluvia()
        texto_evento = fuente.render("¡LLUVIA!", True, AZUL)
        pantalla.blit(texto_evento, (250, 100))
    elif evento_actual == "tormenta":
        pantalla.blit(tormenta_imagen, (0, 0))
        dibujar_tormenta()
        texto_evento = fuente.render("¡TORMENTA!", True, NARANJA)
        pantalla.blit(texto_evento, (230, 100))

# Función para mostrar avisos
def mostrar_aviso():
    tiempo_actual = time.time()
    if aviso and tiempo_actual - tiempo_aviso < duracion_aviso:
        texto_aviso = fuente.render(aviso, True, ROJO)
        ancho_texto = texto_aviso.get_width()
        pantalla.blit(texto_aviso, (ANCHO//2 - ancho_texto//2, 350))

# Inicializar tiempos antes del bucle principal
tiempo_inicio_juego = 0
tiempo_ultimo_evento = 0
tiempo_ultimo_decremento = time.time()
tiempo_ultimo_aumento_dificultad = 0

# Bucle principal
pantalla_actual = "inicio"
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    tiempo_actual = time.time()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_actual == "inicio" and boton_play_rect.collidepoint(evento.pos):
                pantalla_actual = "juego"
                reiniciar_juego()
            elif pantalla_actual == "juego":
                iniciar_arrastre(evento.pos)
            elif (pantalla_actual == "perdido" or pantalla_actual == "ganar") and boton_play_rect.collidepoint(evento.pos):
                pantalla_actual = "inicio"
        if evento.type == pygame.MOUSEBUTTONUP:
            if pantalla_actual == "juego":
                finalizar_arrastre(evento.pos)
        if evento.type == pygame.MOUSEMOTION:
            if pantalla_actual == "juego":
                actualizar_arrastre(evento.pos)

    if pantalla_actual == "inicio":
        mostrar_pantalla_inicio()
        
    elif pantalla_actual == "juego":
        # Actualizar tiempo
        tiempo_actual = time.time()
        if tiempo_inicio_juego > 0:
            tiempo_restante = max(0, 80 - (tiempo_actual - tiempo_inicio_juego))
        
        if plantita["viva"] and tiempo_restante > 0:
            # Fondo base
            pantalla.fill(BLANCO)
            pantalla.blit(fondo_principal, (0, 0))
            # Aplicar efectos de eventos
            if evento_actual:
                aplicar_evento_efectos()
                mostrar_evento()
                
                # Finalizar evento si ha pasado el tiempo
                if tiempo_actual - tiempo_inicio_evento > duracion_evento:
                    finalizar_evento()
            else:
                # Verificar si se genera un nuevo evento
                if tiempo_actual - tiempo_ultimo_evento > intervalo_eventos:
                    if generar_evento():
                        tiempo_ultimo_evento = tiempo_actual
            
            # Decrementar recursos normalmente si no hay evento
            if not evento_actual:
                decrementar_recursos()
            
            # Aumentar dificultad
            aumentar_dificultad()
            
            # Verificar si la planta sigue viva
            verificar_planta_viva()
            
            # Dibujar elementos
            dibujar_plantita()
            dibujar_barras_estado()
            mostrar_aviso()
            
            # Dibujar botones
            pantalla.blit(regadera_imagen, boton_agua_rect.topleft)
            pantalla.blit(abono_imagen, boton_abono_rect.topleft)
            
            # Dibujar indicadores de selección cuando no está arrastrando
            if not arrastrando:
                # Destacar los botones para indicar que se pueden arrastrar
                pygame.draw.rect(pantalla, AZUL, boton_agua_rect, 2)
                pygame.draw.rect(pantalla, VERDE, boton_abono_rect, 2)
                
                # Añadir texto de instrucción
                texto_instruccion = fuente_pequena.render("Arrastra hacia la planta", True, NEGRO)
                pantalla.blit(texto_instruccion, (ANCHO//2 - texto_instruccion.get_width()//2, 330))
            
            # Dibujar objeto arrastrado (por encima de todo)
            dibujar_arrastre()
            
            # Actualizar fase de la plantita y verificar victoria
            if actualizar_fase_plantita():
                pantalla_actual = "ganar"
        elif not plantita["viva"]:
            pantalla_actual = "perdido"
        elif tiempo_restante <= 0:
            pantalla_actual = "ganar"
            
    elif pantalla_actual == "perdido":
        mostrar_pantalla_perdido()
        
    elif pantalla_actual == "ganar":
        mostrar_pantalla_ganar()

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()