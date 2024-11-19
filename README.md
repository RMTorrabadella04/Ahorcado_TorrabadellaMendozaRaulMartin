# Ahorcado 
## Hecho por Raúl Martín Torrabadella Mendoza

El **Juego del Ahorcado** es un divertido desafío de palabras que pone a prueba tu creatividad y conocimiento. En este caso, cuenta con tres temáticas principales: **Frutas**, **Conceptos Informáticos** y **Nombres**.

## Reglas del Juego

1. **Objetivo**: Adivina la palabra secreta antes de completar el dibujo del ahorcado.
2. **Temáticas**: Puedes elegir entre las siguientes categorías:
   - **Frutas**: Palabras relacionadas con frutas, como "manzana" o "plátano".
   - **Conceptos Informáticos**: Términos tecnológicos, como "algoritmo" o "servidor".
   - **Nombres**: Nombres comunes, como "María" o "Carlos".
3. **Dinámica del Juego**:
   - Cada palabra oculta se muestra como una serie de guiones bajos (`_ _ _ _`) que representan sus letras.
   - Los jugadores intentan adivinar una letra por turno. Si aciertan, la letra se revela; si no, se añade una parte al dibujo del ahorcado.
4. **Cómo ganar**: Descubre toda la palabra antes de que se complete el dibujo del ahorcado.

---

## Base de Datos para el Juego

El sistema de juego utiliza una base de datos en **MySQL** para almacenar las palabras y sus categorías.

### Esquema de la Base de Datos

1. **Nombre de la Base de Datos**: `ahorcado`.
2. **Tabla Principales**: `palabras, usuarios, partidas`.
