# Wot Wordle

**Wot Wordle** es un mini-juego de adivinanza de tanques desarrollado en Python usando Tkinter. El objetivo del juego es adivinar un tanque seleccionado al azar de un conjunto definido en un archivo JSON, comparando sus atributos con los del tanque secreto.

---

## Características

- **Selección de tanque:** Escoge un tanque de la lista desplegable (`Combobox`).  
- **Comparación de atributos:**  
  - **Daño:** Indica si es mayor, menor o igual al tanque secreto.  
  - **Velocidad:** Compara usando rangos predefinidos (`veryslow` → `superfast`).  
  - **Clase y Nación:** Verifica si coinciden con el tanque secreto.  
- **Contador de intentos:** Rastrea cuántas veces se ha intentado adivinar.  
- **Retroalimentación visual:** Cambia el fondo de la ventana a verde al acertar y muestra un mensaje emergente.  
- **Reinicio del juego:** Permite seleccionar un nuevo tanque y reinicia los contadores.

---

## Requisitos

- Python 3.x  
- Tkinter (viene incluido con Python)  
- Archivo `tanks.json` con los datos de los tanques  

---

## Uso

1. Clona el repositorio:

```bash
git clone https://github.com/Sagmanua/Wot-Wordle.git
