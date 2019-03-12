# Tutorial para reconhecimento de placas
# Fonte: https://www.youtube.com/watch?v=pDA4mncyJ8Q

import cv2

# Carrega imagem
img = cv2.imread('/home/silvia/PycharmProjects/alex_video/Teste1.png')
#cv2.imshow('teste', img)

# Converte a imagem de colorida para escala de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('teste', cinza)

# Lineariza / binariza a imagem de escala de cinza para preto (limite 90) e branco (limite 255)
_, binario = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
#cv2.imshow('teste', binario)

# Desfoca e elimina ruídos da imagem
desfoque = cv2.GaussianBlur(binario, (5, 5), 0)
#cv2.imshow('teste', desfoque)

# Encontra os contornos da imagem
_, contornos, hierarquia = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print(contornos)
#cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
#cv2.imshow('teste', img)

# Seleciona apenas contornos retangulares / quadrados
for c in contornos:
    # Verifica se o contorno é fechado
    perimetro = cv2.arcLength(c, True)

    if perimetro > 120:

        # Verifica a forma geométrica mais próxima do contorno encontrado
        prox = cv2.approxPolyDP(c, 0.03 * perimetro, True)

        # Seleciona apenas contornos quadriláteros
        if len(prox) == 4:

            (x, y, alt, lar) = cv2.boundingRect(c)

            cv2.rectangle(img, (x, y), (x+alt, y+lar), (0, 255, 0), 2)

            # Recorta e salva a imagem da placa
            roi = img[y: y+lar, x: x+alt]
            cv2.imwrite('/home/silvia/PycharmProjects/alex_video/roi.png', roi)

cv2.imshow('teste', img)

cv2.waitKey(0)
cv2.destroyAllWindows()