texto = input("Digite o texto que deseja encripitar: ").upper()
senha = input("Digite a senha do texto: ").upper()

inicioDoAlfabeto = ord(' ')
tamanhoDoAlfabeto = ord('z')-inicioDoAlfabeto+1

numeroLetrasTexto = [ ord(letra)-inicioDoAlfabeto for letra in texto] #mapeado para numero
numeroLetrasSenha = [ ord(letra)-inicioDoAlfabeto for letra in senha] #mapeado para numero
final = []
for i in range(0, len(numeroLetrasTexto)):
    final.append((numeroLetrasTexto[i] + numeroLetrasSenha[i%len(numeroLetrasSenha)])%tamanhoDoAlfabeto) #parse com senha ps: considera caracteres não letras na hora de iterar senha

print(''.join([chr(letra+inicioDoAlfabeto) for letra in final]))
