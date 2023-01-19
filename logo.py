from PIL import Image 
 
def aggiungi_logo(immagine, logo, nuova_immagine, posizione):
    foto_da_modificare = Image.open(immagine)
    foto_logo = Image.open(logo)
    foto_da_modificare.paste(foto_logo, posizione)
    foto_da_modificare.show()
    foto_da_modificare.save(nuova_immagine)
 
 
if __name__ == '__main__':
    nome_immagine = input("Immagine -> ")
    logo_da_aggiungere = input("Logo -> ")
    aggiungi_logo(nome_immagine, logo_da_aggiungere,
                    'immagine_con_logo.jpg', posizione=(0, 0))