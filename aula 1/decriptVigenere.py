texto = input("Digite o texto que deseja desencripitar: ")
senha = input("Digite a senha do texto: ")

inicioDoAlfabeto = ord(' ')
tamanhoDoAlfabeto = ord('z')-inicioDoAlfabeto+1

numeroLetrasTexto = [ ord(letra) - inicioDoAlfabeto for letra in texto] #mapeado para numero
numeroLetrasSenha = [ ord(letra) - inicioDoAlfabeto for letra in senha] #mapeado para numero
final = []
for i in range(0, len(numeroLetrasTexto)):
    final.append((tamanhoDoAlfabeto + numeroLetrasTexto[i] - numeroLetrasSenha[i%len(numeroLetrasSenha)])%tamanhoDoAlfabeto)

print(''.join([chr(letra+inicioDoAlfabeto) for letra in final]))
