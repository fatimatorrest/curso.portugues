# Definición de personajes

define profesor = Character("Profesora Laura", color="#3366CC")

define narrador = Character(None, italic=True)



# Definición de imágenes
image bg aula:
    "images/aula.jpg"
    zoom 0.8
    xalign 0.5
    yalign 0.5

image bg cafe:
    "images/cafe.jpg"
    zoom 0.8
    xalign 0.5
    yalign 0.5

image bg parque:
    "images/parque.jpg"
    zoom 0.8
    xalign 0.5
    yalign 0.5

image bg biblioteca:
    "images/biblioteca.jpg"
    zoom 0.8
    xalign 0.5
    yalign 0.5



# Definición del profesor (usando la imagen proporcionada)

image profesor = "images/profesor.jpg"



# Inicio del juego

label start:


    # Escena 1: Presentación

    scene bg aula

    show profesor at center

    

    profesor "Benvindo! Bienvenidos a nuestra lección. Hoy aprederemos saludos en portugués."

    profesor "Mi nombre es Profesora Maria y te ayudaré en este aprendizaje."

    

    # Escena 2: Buenos dias y cafe 

    scene bg cafe with dissolve

    show profesor at center

    
    profesor "Imaginemos que entras a una cafetería en Lisboa..."

    profesor "Primero, saludas con: 'Bom dia / Boa tarde.' (Buenos días / Buenas tardes)"

    profesor "Luego dices: 'Um cafe, se faz favor' (Un café, por favor)"

    profesor "¡Eso es todo! Has sido educado y claro. Bien hecho." 

    
   # Escena 3: Donde esta algo

    scene bg parque with dissolve

    show profesor at center

    
    profesor "Ahora aprenderemos cómo preguntar dónde está algo."
   
    profesor "Por ejemplo: 'Onde fica o parque?' (¿Dónde está el parque?)"

    profesor "onde = dónde, fica = está.  Fácil, ¿verdad?"

    

    # Escena 4: Despedidas

    scene bg biblioteca with dissolve

    show profesor at center

    

    profesor "Ahora estamos en la biblioteca. Vamos a aprender cómo preguntar por un libro."

    profesor "Puedes decir: 'Tem o livro de Harry Potter?' (¿Tienen un libro?)"

    profesor "'Tem' significa '¿tienen?' y 'livro''un libro'."

    

    # Menú de preguntas 

    profesor "Ahora, vamos a poner a prueba lo que has aprendido."

    

    menu:

        profesor "¿Cómo se dice, buenos dias?"

        "Ate logo":

            jump respuesta_incorrecta

            

        "Bom dia":

            jump respuesta_correcta

            

        "Boa noite":

            jump respuesta_incorrecta

    
 # Escenas de resultado

    label respuesta_correcta:

        scene bg aula with dissolve

        show profesor at left


        profesor "¡Výborně! (¡Excelente!)"

        profesor "Has elegido la manera correcta para decir buenos dias"

        profesor "¡Felicidades por completar esta lección básica de frases comunes en checo!"

        return

        

    label respuesta_incorrecta:

        scene bg aula with dissolve

        show profesor at right


        profesor "To není správně. (Eso no es correcto.)"

        profesor "Puedes volver a intearlo."

        profesor "¡Sigamos practicando para mejorar!"

        return

