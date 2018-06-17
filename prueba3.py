from selenium import webdriver
import datetime
import time
from scapOk import Hilo

def responderAws(arr):
    for a in arr:
        res = h1.getApiRespuesta(a)
        ires =  "?_ " + a + "\n"
        ires += "!_ " + res + "\n"
        ires += "-------------- \n"

        print(res)


def nombreArchivo(vclienteId):
    return (vclienteId + "_"+ str(datetime.datetime.utcnow()).strip()[0:15].replace('-','').replace(' ','').replace(':',''))


"""
Init --------------------------------

"""

h1 = Hilo("1")

print("1. Comenzandando ...")

driver = webdriver.Chrome('./chromedriver')

driver.get('http://web.whatsapp.com')

input("Escanee el código QR ........... \n")

#conversa = driver.find_element_by_xpath('//span[@class = "selectable-text"]')

#velemento = "selectable-text invisible-space copyable-text"
velemento = "selectable-text"

#conversas = driver.find_elements_by_xpath('//span[@class = "{}"]'.format(velemento))

#all_spans = driver.find_elements_by_xpath("//span[@class='{}']".format(velemento))

# Acá tiene que arrancar el buble

while True:

    all_spans = driver.find_elements_by_xpath('//span[@class]')


    input("stop --------------------\n")

    vinit = "_init"

    lineDesde = 0
    lineHasta = 0
    lineActual = 0 

    charla = []
    respuestasNuevas = []
    wf = open(nombreArchivo("1")+".log", "w")
    tomar = False

    ri = 0
    pi = 0

    # palabras que no quiero relevar 
    palabrasNo = ['','HOY','AYER','LUNES','MARTES','MIERCOLES']

    for span in all_spans:

        lin = span.text

        print ("\n >> ", lin)
        print (" ??? ", span.get_attribute('class'))

        # --- saco los dialogos que no van
        v1 = lin[2:3]==":"
        #v2 = lin[0:1]=="_ " # son mis conversaciones
        v3 = lin.strip() in palabrasNo
        v4 = 0 < span.get_attribute('class').find('selectable-text')
        


        if (vinit == lin.strip()):
            tomar = True
            print(" **************************************************************** ")
            print(" Arranca con: ", lin)
            print(" **************************************************************** ")


        if (not (v1 or v3 or v4) and tomar):

            lineActual += 1 

            if (lineActual > lineHasta):  #verifico si estoy en alguno nuevo

                lineHasta += 1


                if (lin[0:1]=="_"):
                    pr="P"+str(pi)+": "
                    pi += 1
                else:
                    pr="R"+str(ri)+": "
                    ri += 1
                    respuestasNuevas.append(lin)

                
                vvalor = pr+lin
                charla.append(vvalor)
                wf.write(vvalor)

                wf.write('\n')
                print ("\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  ", lin)
    
    print("Esperando por timer ....")
    
    responderAws(respuestasNuevas) # manda las respuestas nuevas

    time.sleep(5)
