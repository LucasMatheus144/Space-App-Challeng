import cv2
import sys

planeta_lixo_espacial = cv2.imread(sys.argv[0])
planeta_terra_limpo = cv2.imread(sys.argv[0])

diferenca = cv2.subtract(planeta_lixo_espacial,planeta_terra_limpo)

print(f"As imagems {sys.argv[0]} e {sys.argv[0]} sao >",end='')
if diferenca:
    print("iguais")
else:
    print("diferentes")
    cv2.imshow(f"Diferenças encontradas",diferenca)
    cv2.waitKey(1)