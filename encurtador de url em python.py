import pyshorteners

# URL a ser encurtada
url = "https://www.google.com"

# Cria um objeto Shortener
s = pyshorteners.Shortener()

# Encurta a URL usando o serviço padrão (ou seja, bit.ly)
short_url = s.bitly.short(url)

# Imprime a URL encurtada
print("URL encurtada:", short_url)
