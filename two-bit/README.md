# Serial Test en Python (Two-Bit Test)  

![Python](https://img.shields.io/badge/Python-3.13.2-blue.svg)  
![Status](https://img.shields.io/badge/Estado-Completado-success)  

## Descripción  
Este proyecto implementa la **prueba serial (Two-Bit Test)** en Python para evaluar la pseudoaleatoriedad de una secuencia de bits. La prueba analiza la frecuencia de los pares `00`, `01`, `10`, y `11`, calculando un estadístico **\(X^2\)** basado en la distribución **\(\chi^2\)**.  

## Objetivo  
Determinar si una secuencia de bits generada es pseudoaleatoria utilizando pruebas estadísticas.  

## Requisitos  
- Python **3.13.2**  
- Librerías estándar de Python (`math`, `os`)  

## Estructura del Proyecto  
    two-bit
    |--- main.py
    |--- serial_test.py
    |--- henon_output
    |   |--- binarios.txt
    |--- README.md

## Instalación y uso
1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/Grum5/Simulaci-n.git
    cd Simulaci-n/two-bit
    ```
2. **Ejecutar el script**
    ```bash
    python3 main.py
    ```

