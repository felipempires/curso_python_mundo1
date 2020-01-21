#\033[style;  text;  back m
# 0 = none
# 1 = bold
# 4 = underline
# 7 = negative (inverte frente fundo)

# 30 ou 40 = branco
# 31 ou 41 = vermelho
# 32 ou 42 = verde
# 33 ou 43 = amarelo
# 34 ou 44 = azul
# 35 ou 45 = mangenta
# 36 ou 46 = siena
# 37 ou 47 = cinza


print(f' \033[0;30;41m Teste \033[0;0;0m')
print(f' \033[7;30m Teste \033[0;0;0m')