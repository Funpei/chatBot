from selenium import webdriver
import time
import datetime

def nombreArchivo(vclienteId):
    return (vclienteId)

def timeStamp():
    return (str(datetime.datetime.utcnow()).strip()[0:15].replace('-','').replace(' ','').replace(':',''))


class Hilo:
    
    def enviarAws(self, vdato):
        if (vdato.strip()!=""):
            msg_box = driver.find_element_by_class_name('_2S1VP')
            if (vdato != vinit2): 
                vts = "-"+timeStamp()
            else:
                vts = ""

            msg_box.send_keys(vdato + vts + "-")
            driver.find_element_by_class_name('_2lkdt').click()
            archLog.write("\n  .. enviando: " + vdato + "-")
            
    
    def ultMensaje(self):

        all_spans = driver.find_elements_by_xpath('//span[@class]')


        lineDesde = 0
        lineHasta = 0
        lineActual = 0 

        charla = []
        respuestasNuevas = []

        tomar = False

        ri = 0
        pi = 0

        # palabras que no quiero relevar 
        palabrasNo = ['','HOY','AYER','LUNES','MARTES','MIERCOLES','Activar notificaciones de escritorio']
        mensajesNo1 = "Los mensajes de este grupo ahora"


        archLog.write("\n --- Buscando ultimas respuestas:")

        for span in all_spans:
            try:
                lin = span.text

                print ("\n >> ", lin)
                #print (" ??? ", span.get_attribute('class'))

                # --- Filtros ------------------------------------------------
                v1 = lin[2:3]==":"
                #v2 = lin[0:1]=="_ " # son mis conversaciones
                v3 = lin.strip() in palabrasNo
                v4 = -1 < span.get_attribute('class').find('selectable-text')
                v5 = -1 < lin.find(mensajesNo1)
                v6 = lin[len(lin)-1:len(lin)]=='-'
                v7 = -1 < span.get_attribute('class').find('_2wP_Y')
                v8 = -1 < span.get_attribute('class').find('_')
                v9 = -1 < span.get_attribute('dir').find('auto')
                # -------------------------------------------------------------

                print("\n ? Comparando si encuentra el init chatbot: ", vinit , "  == ", lin.strip())
                
                if self.lineHasta > 0:  # ya lo había encontrado el inicio de chat
                    archLog.write("\n    -- Ya fue encontrado el *inicio chat " + str(self.lineHasta))
                    tomar = True
                else:                   # todavía no encontró inicio de chat para este hilo.
                    if (vinit == lin.strip()):
                        tomar = True
                        print(" **************************************************************** ")
                        print(" Arranca con: ", lin)
                        print(" **************************************************************** ")
                        archLog.write("\n --- Encontró el inicio chatbot-")


                if (not (v1 or v3  or v5 or v6 or v7 or v8 or v9) and tomar and v4):

                    lineActual += 1 
                    archLog.write("\n ---89--- Linea buscada: "+ lin + "  --- " + str(lineActual) + " LineHasta en el Hilo: " + str(self.lineHasta) + " class : " + span.get_attribute('class'))
                    
                    print("\n -89--- Linea buscada: "+ lin + "  --- " + str(lineActual) + " LineHasta en el Hilo: " + str(self.lineHasta) + " class : " + span.get_attribute('class'))
            

                    if (lineActual > self.lineHasta):  #verifico si estoy en alguno nuevo

                    
                        archLog.write("\n --- Linea encontrada : "+ lin + " --- " + str(lineActual) + "  lineHasta: " +str(self.lineHasta))


                        if (lin[0:1]=="_"):
                            pr="P"+str(pi)+": "
                            pi += 1
                        else:
                            pr="R"+str(ri)+": "
                            ri += 1
                            respuestasNuevas.append(lin)
                        
                        vvalor = pr+lin
                        if vvalor != vinit:
                            charla.append(vvalor)
                            break  # panic sacar que porco solo recupera una linea

            except Exception as e:
                archLog.write("\n 97 Levanta exception ....."+ str(e))
                
        
        self.lineHasta = lineActual
        
        archLog.write("\n                  -- self.lineHasta: " + str(self.lineHasta))

        archLog.write("\n                  -- lineActual: " + str(lineActual))


        # termina de recorrer 
        if respuestasNuevas == []:
            respuestasNuevas = ['None']

        archLog.write("\n----- Respuestas detectadas: " + str(respuestasNuevas))

        return respuestasNuevas
                   
    
    def log(self,lup,lur):
        vna = nombreArchivo(self.clienteId)
        wf = open(vna+".log", "a")
        wf.write("\n" + str(lup)) # guardo la ultima pregunta
        wf.write("\n" + str(lur)) # guardo la ultima respuesta
    
    def getApiRespuesta(self, lum):
        # Acá tengo que poner la APi de Andrés
        archLog.write("\n-------- La API toma estas preguntas :")
       
        archLog.write("\n"+str(lum))
       
        archLog.write("\n-------- La API le responde esto: ")
       
        vrespuesta = "\n Respondiendo ("+str(lum)+")"
       
        archLog.write(vrespuesta)

        return vrespuesta
    
    def __init__(self,clienteId):

        self.lineDesde = 0 # linea donde comienza el chat 
        self.lineHasta = 0 # ultima linea relevada del chat
        self.clienteId = clienteId
        archLog.write("\n---- Instanciando Hilo para el contacto: "+ clienteId)
        
        # inicializo el chat 
        select_contacto(clienteId)
        self.enviarAws("inicio chatbot")

contactos = [] #guardos todos los hilos por contactos
contactos_nombres = [] #lista de los nombres de contactos


def init():

    arch = open("contactos.txt","r")
    contactos_nombres = eval(arch.read())

    print(" Contactos a encuestar: " + str(contactos_nombres))
    
    archLog.write("\n-1. ---- Contactos a encuestar:")
    archLog.write("\n"+str(contactos_nombres)+"\n\n")


    for cn in contactos_nombres:
        contactos.append(Hilo(cn))


def select_contacto(clienteId):


    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(clienteId))
        user.click()

        archLog.write("\n  !!!!!!!!!!!!!!!!!!!! " + user.get_attribute('title') + " ---- " + user.get_attribute('class') )
    
        time.sleep(3)

       # user.click()

        archLog.write("\n----- Seleccionando el contacto:")
        archLog.write("\n"+clienteId)
    except:
        archLog.write("\n *********** Exception al querer seleccinar en contacto: "+clienteId)
        pass    
        
def schedule():
    #0. seleccionando contactos
    while True:
        for contacto in contactos:

            select_contacto(contacto.clienteId)

            lup = contacto.ultMensaje()  #2. ultima pregunta
            lur = contacto.getApiRespuesta(lup) #3. ultima respuesta
            contacto.log(lup,lur) #3. actualizar el log
            contacto.enviarAws(lur)

        global nro_etapa 
        nro_etapa += 1


        valor = input('Se completó la etapa {} del diálogo seleccionado. \n Presione tecla para continuar o escriba salir para finalizar \n'.format(nro_etapa))
        

        if (valor.upper()=='salir'.upper()):
            break

def start():

    
    #input('STOP')


    driver.get('http://web.whatsapp.com')

    input("Escanee el código QR y presione una tecla \n\n")

    init()

    input("Fueron inicializados todos los chats de los contactos. \n. Presione una tecla para continuar. \n")


    archLog.write("\n \n \n -----------------------------------------\n")
    archLog.write(" -------------- Comiendaza el chat ---------------\n")
    archLog.write("-----------------------------------------\n\n\n")

    #input('Escanee el código QR y luego presione una tecla')
    
    schedule()

    print("Finalizando ............... ")


if __name__ == "__main__":
    
    nro_etapa = 0 

    vinit = "inicio chatbot-"
    vinit2 = "inicio chatbot"

    archLog = open("log.txt","w")
    archLog.write("Iniciando .... \n")

    driver = webdriver.Chrome('./chromedriver')

    start()