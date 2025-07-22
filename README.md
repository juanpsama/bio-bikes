
## 🚵 **Bio-bikes: Analiza y Mejora Tu Técnica Ciclista** 

Bio-bikes es un proyecto que utiliza Python, Tkinter para la UI, OpenCV y los modelos de detección de pose de [Mediapipe](https://github.com/google/mediapipe) para optimizar el rendimiento y prevenir lesiones en deportistas. 📸

Bio-bikes genera una lectura goniométrica, identificando cuales son los puntos máximos de la extensión de las articulaciones involucradas en la pedalada. Esta aplicación genera análisis goniométricos y antropométricos, identificando áreas de mejora 💪.
## 🚀 Instrucciones para ejecutar el proyecto

1. **Crear el archivo `.env`**
   - Copia el contenido de `.env.save` y crea un archivo `.env` en la raíz del proyecto.
   - Asegúrate de que la variable `DATABASE_URL` sea:
     ```
     DATABASE_URL=sqlite:///gfg.db
     ```

2. **Crear un entorno virtual de Python**
   ```sh
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   - En Windows:
     ```sh
     venv\Scripts\activate
     ```

4. **Instalar los paquetes requeridos**
   ```sh
   pip install -r requirements.txt
   ```

5. **Correr las migraciones de la base de datos**
   ```sh
   alembic upgrade head
   ```

6. **Ejecutar la aplicación**
   ```sh
   python -m app
   ```
