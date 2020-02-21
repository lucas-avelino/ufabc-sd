texto = input("Digite o texto que deseja encripitar: ").upper()
senha = input("Digite a senha do texto: ").upper()

numeroLetrasTexto = [ ord(letra)-65 for letra in texto] #mapeado para numero
numeroLetrasSenha = [ ord(letra)-65 for letra in senha] #mapeado para numero
final = []
for i in range(0, len(numeroLetrasTexto)):
    final.append((numeroLetrasTexto[i] + numeroLetrasSenha[i%len(numeroLetrasSenha)])%26) #parse com senha ps: considera caracteres não letras na hora de iterar senha

print(''.join([chr(letra+65) for letra in final]))
