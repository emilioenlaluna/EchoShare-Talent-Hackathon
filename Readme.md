# EchoShare - Interfaz de WhatsApp

## Descripción
EchoShare es un proyecto desarrollado por el equipo Honey como parte del track de Salud Digna. La finalidad de este proyecto es facilitar la extracción y envío de imágenes de ultrasonido a través de WhatsApp, garantizando la privacidad del paciente y mejorando su experiencia en la recepción de resultados de estudios médicos.

## Funcionalidades
- Extracción de imágenes de ultrasonido.
- Envío seguro de imágenes y vídeos de estudios de ultrasonido a través de WhatsApp.
- Gestión de datos de ultrasonido mediante inteligencia artificial.
- Recepción sencilla de resultados por parte del usuario.
- Comunicación más eficiente y personalizada con los pacientes.

## Requisitos
Para ejecutar la interfaz de WhatsApp de EchoShare, se necesitan los siguientes requisitos previamente instalados:
- Python 3.x
- Biblioteca Twilio para Python (se puede instalar utilizando pip: `pip install twilio`)
- Cuenta de Twilio con acceso a la API de WhatsApp
- Configuración de webhooks en la cuenta de Twilio para recibir mensajes de WhatsApp

## Configuración
1. Clone el repositorio de EchoShare: `git clone https://github.com/honey-team/echoshare.git`
2. Navegue hasta el directorio del proyecto: `cd echoshare`
3. Copie el archivo de configuración de ejemplo: `cp config.example.py config.py`
4. Edite el archivo `config.py` con sus credenciales de Twilio y demás configuraciones necesarias.
5. Asegúrese de tener acceso a internet para que el servidor pueda recibir y enviar mensajes a través de WhatsApp.

## Uso
Una vez configurado, puede ejecutar la interfaz de WhatsApp de EchoShare ejecutando el siguiente comando en la terminal:

# Contribución
¡Estamos abiertos a contribuciones! Si desea contribuir al proyecto, por favor, envíe un pull request en GitHub.

## Soporte
Si necesita ayuda o tiene alguna pregunta, no dude en abrir un issue en el repositorio de GitHub.

## Licencia
Este proyecto está bajo la licencia MIT. Consulte el archivo LICENSE para obtener más detalles.