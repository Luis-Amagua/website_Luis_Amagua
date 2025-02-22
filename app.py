from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Instanciamos el traductor
translator = Translator()

# Definir el texto en español
presentacion = """
Hola, soy Luis, Ingeniero Matemático y actualmente estudio una maestría en Inteligencia Artificial Aplicada en la UHE. 
Con más de 3 años de experiencia en análisis de datos utilizando R, Python, SQL y Power BI, he trabajado en proyectos de segmentación de clientes y análisis bancarios. 
He aplicado técnicas de machine learning y programación dinámica en aprendizaje por refuerzo, además de explorar NLP en análisis de texto. 
Tengo conocimientos en Git y Docker, lo que mejora mi flujo de trabajo. Me apasiona seguir aprendiendo y trabajando en proyectos de inteligencia artificial.
"""
adicionales="""Durante mi etapa de pregrado, participé activamente en diversas iniciativas. Fui parte de Data Skills, una escuela de formación especializada 
en herramientas de análisis de datos, donde impartí capacitaciones en RStudio, Power BI y Excel. Además, fui miembro fundador del Club de Turismo Politécnico en la Escuela Politécnica Nacional de Ecuador, contribuyendo al desarrollo de proyectos y actividades orientadas al fortalecimiento de las habilidades de comunicación y trabajo en equipo de los estudiantes.
"""



# Función para traducir el texto automáticamente al idioma seleccionado
def translate_text(text, lang='en'):
    translation = translator.translate(text, dest=lang)
    return translation.text

@app.route('/')
def index():
    lang = request.args.get('lang', 'es')  # Obtener el idioma de la URL, por defecto 'es' (español)
    
    # Si el idioma es inglés, traducimos el texto
    text_presentacion  = translate_text(presentacion, lang) if lang == 'en' else presentacion
    text_adicionales= translate_text(adicionales, lang) if lang == 'en' else adicionales

    #index
    return render_template('index.html', 
                           text_presentacion=text_presentacion, 
                           text_adicionales=text_adicionales, 
                           lang=lang)

def proyects():
    lang = request.args.get('lang', 'es')  # Obtener el idioma de la URL, por defecto 'es' (español)
    
    # Si el idioma es inglés, traducimos el texto
    text_presentacion  = translate_text(presentacion, lang) if lang == 'en' else presentacion
    text_adicionales= translate_text(adicionales, lang) if lang == 'en' else adicionales

    
    return render_template('projects.html', 
                           text_presentacion=text_presentacion, 
                           text_adicionales=text_adicionales, 
                           lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
