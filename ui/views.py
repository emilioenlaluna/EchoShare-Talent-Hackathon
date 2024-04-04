from datetime import timezone
from django.shortcuts import render
from core.models import Paciente, EstudioUltrasonido, ImagenUltrasonido
from django.shortcuts import get_object_or_404, render
from core.models import EstudioUltrasonido, ImagenUltrasonido

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
#
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError

#
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
#
from django.contrib.auth.forms import AuthenticationForm
#
from django.contrib.auth.decorators import login_required
#
from django.apps import apps
#
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html' )

@login_required
def dashboard(request):
    return render(request, 'usuario/dashboard.html' )


def ver_ultrasonidos(request, id_paciente):
    # Buscar al paciente por su ID
    paciente = Paciente.objects.get(idPaciente=id_paciente)

    # Obtener todos los estudios de ultrasonido relacionados con el paciente
    estudios_ultrasonido = EstudioUltrasonido.objects.filter(Paciente=paciente)

    # Obtener todas las imágenes de ultrasonido asociadas a cada estudio
    imagenes_ultrasonido = ImagenUltrasonido.objects.filter(EstudioUltrasonido__in=estudios_ultrasonido)

    # Preparar el contexto con la información a mostrar
    contexto = {
        'paciente': paciente,
        'estudios_ultrasonido': estudios_ultrasonido,
        'imagenes_ultrasonido': imagenes_ultrasonido,
    }

    # Renderizar la respuesta utilizando una plantilla
    return render(request, 'ultrasonidos/ver_ultrasonidos.html', contexto)



def detalle_ultrasonido(request, id_paciente, estudio_id):
    estudio = get_object_or_404(EstudioUltrasonido, idEstudioUltrasonido=estudio_id, Paciente__idPaciente=id_paciente)
    imagenes = ImagenUltrasonido.objects.filter(EstudioUltrasonido=estudio)

    return render(request, 'ultrasonidos/detalle_ultrasonido.html', {
        'estudio': estudio,
        'imagenes': imagenes,
    })



@login_required
def crearcuenta(request):
    if request.method == 'GET':
        return render(request, 'auth/crearcuenta.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'crearcuenta.html', {'form': UserCreateForm, 'error': 'Nombre de usuario ya en uso. Elija a otro nombre de usuario.'})
        else:
            return render(request, 'auth/crearcuenta.html',
                          {'form': UserCreateForm,
                           'error': 'Las contraseñas son diferentes'})

@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('home')


def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, 'auth/iniciarsesion.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
        username=request.POST['username'],
        password=request.POST['password']) 
        if user is None:
            return render(request,'auth/iniciarsesion.html',{'form': AuthenticationForm(), 'error': 'Esta cuenta no existe en nuestro registros'})
        else: 
            login(request,user)
            return redirect('home')


def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        try:
            paciente = Paciente.objects.get(Correo=correo)
            user = paciente.usuario
            usuario_autenticado = authenticate(request, username=user.username, password=contrasena)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Credenciales inválidas'})
        except Paciente.DoesNotExist:
            return render(request, 'login.html', {'error': 'Correo electrónico no registrado'})
    else:
        return render(request, 'auth/login.html')

def login_with_token(request):
    token = request.GET.get('token')
    try:
        estudio = EstudioUltrasonido.objects.get(token=token)
        if estudio.fecha_expiracion_token < timezone.now():
            return redirect('token_expired')

        paciente = estudio.Paciente
        user = paciente.usuario
        usuario_autenticado = authenticate(request, username=user.username, password='la_contraseña_del_usuario')
        if usuario_autenticado is not None:
            login(request, usuario_autenticado)
            return redirect('dashboard')
    except EstudioUltrasonido.DoesNotExist:
        return redirect('token_invalid')
    
from django.shortcuts import render, get_object_or_404
from core.models import VideoUltrasonido

def mostrar_video(request, video_id):
    video = get_object_or_404(VideoUltrasonido, idVideoUltrasonido=video_id)
    return render(request, 'mostrar_video.html', {'video': video})


from django.shortcuts import render
import pydicom

from core.models import ImagenUltrasonido

def view_dicom(request, imagen_id):
    imagen = ImagenUltrasonido.objects.get(pk=imagen_id)
    ds = pydicom.dcmread(imagen.Imagen.path)
    # Aquí puedes procesar y visualizar el archivo DICOM utilizando las funciones de pydicom
    return render(request, 'view_dicom.html', {'ds': ds})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from dotenv import load_dotenv
import os

@csrf_exempt
def verificar_webhook(request):
    if request.method == 'GET':
        try:
            token = request.GET.get('hub.verify_token')
            challenge = request.GET.get('hub.challenge')
            load_dotenv()
            WEBHOOKTOKEN = os.getenv('WEBHOOKTOKEN')
            WEBHOOKTOKEN = str(WEBHOOKTOKEN) if WEBHOOKTOKEN else "echosharestorage"
            if token == WEBHOOKTOKEN and challenge:
                return JsonResponse({'hub.challenge': challenge})
            else:
                return JsonResponse({'error': 'Conexión con META incorrecta :c'}, status=403)
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=403)

@csrf_exempt
def recibir_mensajes(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            entry = body['entry'][0]
            changes = entry['changes'][0]
            value = changes['value']
            message = value['messages'][0]
            number = message['from']
            text = obtener_texto(message)
            response = respuestas_bot(text, number)
            return JsonResponse({'status': 'success', 'message': 'Mensaje respondido :3', 'response': response, 'from': number, 'text': text})
        except Exception as error:
            return JsonResponse({'status': 'error', 'message': 'Mensaje no enviado', 'error': str(error)})

def obtener_texto(message):
    type_message = message.get('type', None)
    if type_message == 'text':
        return message['text']['body']
    elif type_message == 'button':
        return message['button']['text']
    elif type_message == 'interactive':
        if message['interactive']['type'] == 'list_reply':
            return message['interactive']['list_reply']['title']
        elif message['interactive']['type'] == 'button_reply':
            return message['interactive']['button_reply']['title']
    return 'Mensaje no procesado :c'

import requests
import json
def respuestas_bot(text, number):
    saludo = ['hola', 'Hola', 'ola', 'buen']
    horario_keywords = ['hora', 'horario', 'cuándo', 'cuando']
    consultar_sin_ticket = "consultar sin ticket"
    lugar_keywords = ['lugar', 'localización', 'localizacion', 'dónde', 'donde']
    text = text.lower()
    if any(keyword in text for keyword in saludo):
        url = "https://graph.facebook.com/v18.0/274158172446307/messages"
        payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "524492680840",
        "type": "text",
        "text": {
            "preview_url": False,
            "body": "¡Hola! 👋 Soy el Asistente Virtual de Salud Digna.🤖"
        }
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EAADbpgLcRG4BO8Jyl39W3JdnjTwdeJbYYyM0mstLJSpuFZClwcdH0mxIz2JZBQ30KaLrF6aX79OwJZCyHYgH5ihaN1JASziHgF7FONZCxZCjBXyE9b28QAYbWSwLQdgMdpnO6qSRkPEih2cAm9Mm9zlYsjFBVC7et6dGLO8Ml33XzJTaNPuyC1RWrAZCEzJfJ4HDkFdTywxDRLxZC6Drx1U02Dbdt46J0N8xgpKQGzAs19ZAOho3VoSP'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        
        import requests
        import json

        url = "https://graph.facebook.com/v18.0/274158172446307/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": "524492680840",
        "recipient_type": "individual",
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
            "text": "<Body Text>"
            },
            "action": {
            "buttons": [
                {
                "type": "reply",
                "reply": {
                    "id": "001",
                    "title": "Consulta de Resultados con ticket"
                }
                },
                {
                "type": "reply",
                "reply": {
                    "id": "002",
                    "title": "Consulta de Resultados sin ticket"
                }
                },
                
            ]
            }
        }
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EAADbpgLcRG4BO8Jyl39W3JdnjTwdeJbYYyM0mstLJSpuFZClwcdH0mxIz2JZBQ30KaLrF6aX79OwJZCyHYgH5ihaN1JASziHgF7FONZCxZCjBXyE9b28QAYbWSwLQdgMdpnO6qSRkPEih2cAm9Mm9zlYsjFBVC7et6dGLO8Ml33XzJTaNPuyC1RWrAZCEzJfJ4HDkFdTywxDRLxZC6Drx1U02Dbdt46J0N8xgpKQGzAs19ZAOho3VoSP'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        
        
        
        
        

    elif any(keyword in text for keyword in lugar_keywords):
        message = "Laboratorio 204 de la Universidad Autónoma de Aguascalientes 🧐\nTambién transmitimos las clases en vivo en Youtube:\nhttps://www.youtube.com/@ClubDeProgramacionCreativa/streams"
    elif any(keyword in text for keyword in lugar_keywords):
        message = "Laboratorio 204 de la Universidad Autónoma de Aguascalientes 🧐\nTambién transmitimos las clases en vivo en Youtube:\nhttps://www.youtube.com/@ClubDeProgramacionCreativa/streams"
    elif consultar_sin_ticket in text:
        # Código para manejar la consulta sin ticket
        
        import requests
        import json

        url = "https://graph.facebook.com/v18.0/274158172446307/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "524492680840",
        "type": "text",
        "text": {
            "preview_url": False,
            "body": """Para consultar tus resultados o estatus de lentes sigue estas indicaciones:
                    🔸 Envia una foto del código de barras de tu ticket.
                    🔸 Si lo prefieres, puedes escribir el RSV u OPC de tu ticket. 

                    Ejemplo ⬇"""
        }
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EAADbpgLcRG4BO8Jyl39W3JdnjTwdeJbYYyM0mstLJSpuFZClwcdH0mxIz2JZBQ30KaLrF6aX79OwJZCyHYgH5ihaN1JASziHgF7FONZCxZCjBXyE9b28QAYbWSwLQdgMdpnO6qSRkPEih2cAm9Mm9zlYsjFBVC7et6dGLO8Ml33XzJTaNPuyC1RWrAZCEzJfJ4HDkFdTywxDRLxZC6Drx1U02Dbdt46J0N8xgpKQGzAs19ZAOho3VoSP'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    else:
        message = "*¡Bienvenido al Club de Programación Creativa!* 🐈\nSomos un grupo de apasionados por la automatización y los bots. Creamos proyectos y aprendemos programación.\nPregúntame lo que necesites y no olvides suscribirte a https://youtu.be/mLpH-yDq9Z4?si=oasYM8ZfVumKA4tm"
    

def enviar_mensaje(message_json):
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    ENDPOINT = os.getenv('ENDPOINT')
    try:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN}
        response = requests.post(ENDPOINT, headers=headers, data=message_json)
        if response.status_code == 200:
            return 'Mensaje enviado :3'
        else:
            return 'Mensaje no enviado :3', response.status_code
    except Exception as error:
        return error, 403

def formato_texto(number, text):
    message = json.dumps(
        {
            'messaging_product': 'whatsapp',    
            'recipient_type': 'individual',
            'to': number,
            'type': 'text',
            'text': {
                'body': text
            }
        }
    )
    return message


from django.shortcuts import render

def facial_login_view(request):
    return render(request, 'facial_login.html')

def success(request):
    return render(request, 'success.html')


from django.shortcuts import render, get_object_or_404
from core.models import EstudioUltrasonido, ImagenUltrasonido, VideoUltrasonido

def estudio_ultrasonido_detalle(request, id_estudio):
    estudio = get_object_or_404(EstudioUltrasonido, idEstudioUltrasonido=id_estudio)
    imagenes = ImagenUltrasonido.objects.filter(EstudioUltrasonido=estudio)
    videos = VideoUltrasonido.objects.filter(EstudioUltrasonido=estudio)

    context = {
        'estudio': estudio,
        'imagenes': imagenes,
        'videos': videos,
    }

    return render(request, 'estudio_ultrasonido_detalle.html', context)


from django.shortcuts import render
from django.http import HttpResponse

def compartir_archivos(request):
    if request.method == 'POST':
        import requests
        import json

        url = "https://graph.facebook.com/v18.0/274158172446307/messages"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer EAAU4e4IF7y4BO5LQj083l83ZCgWWzWeIpV9wsXWJiiIhZB3O3AKxqCkLXAnSGHtdlpiTxi1YcUIe2SVE7YAnALzofQV3XCu6NXEZAxlywVrEwgZC0HcWlyZA2KwkBPMZAGH5oyrNsjCMYR3jlb2IB4wiVlgfySm5MHD8ZCkufXbdEHgJ6arVVPXqBMdbi6RyzjZBboIr1lWdggZCkWu0Mp9uesaC4K8cDYA63xEwZD'
        }

        image_urls = [
            "https://echosharestorage.blob.core.windows.net/media/imagenes/Ecografia_2D_embarazo_de_94_semanas.jpg",
            "https://echosharestorage.blob.core.windows.net/media/imagenes/ecografia-embrion-semana-8.jpg",
            "https://echosharestorage.blob.core.windows.net/media/imagenes/Embarazo_de_7_semanas_en_2D_y_3D.jpg",
            "https://echosharestorage.blob.core.windows.net/media/imagenes/eco1.jpg"
        ]

        for image_url in image_urls:
            payload = json.dumps({
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": "524493877620",
                "type": "image",
                "image": {
                    "link": image_url
                }
            })

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            # Obtener la URL de la vista anterior desde la solicitud
            url_anterior = request.META.get('HTTP_REFERER')

            # Redireccionar al usuario a la URL anterior
            return redirect(url_anterior)

        url_anterior = request.META.get('HTTP_REFERER')

        # Redireccionar al usuario a la URL anterior
        return redirect(url_anterior)