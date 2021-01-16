# Se importan librerias a utilizar.
import httplib2
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Ingresar el id del usuario en user_id.
# bin_url contiene el url directo a los usuarios.
user_id = '22656'
bin_url = f'http://stackoverflow.com/users/{user_id}?tab=tags'

# Se inicializa una variable que esta lista para hacer llamadas por protocolo http
http = httplib2.Http()

# Se realiza una request http te tipo Get a la url antes mensionada devolviendonos la pagina del usuario.
# Se obtiene la cabecera y el contenido de la pagina en bruto.
resp, data = http.request(bin_url, method='GET')

# El contenido d ela pagina se codifica de bytes a string.
html = data.decode('UTF-8')

# BeutifulSoup organiza el archivo para que sea facil obtener informacion.
soup = BeautifulSoup(html)

# Por medio de Beautifulsoup obtenemos los tags del usuario.
tags = soup.select('table.user-tags tbody a')

#Para poder desplegar la imformacion, guardamos los tags como un solo string con espacios entre ellos.
data = ' '

for tag in tags:
  data = f'{data}{tag.text} '

print(data)

# Wordcloud se encarga de generar la imagen.
worlcloud = WordCloud().generate(data)

# matplotlib se encarga de desplegar la imagen.
plt.imshow(worlcloud)
plt.axis('off')
plt.show()
