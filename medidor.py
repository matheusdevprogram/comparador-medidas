medidas = {
            'torax':'',
            'busto':'',
            'ombros':'',
            'cintura':'',
            'quadril':'',
            'gluteo':'',
            'coxa_d':'',
            'coxa_e':'',
            'panturrilha_d':'',
            'panturrilha_e':'',
            'braco_d':'',
            'braco_e':''
 }

for chave in medidas:
    medidas[chave]= float(input(f"Digite sua medida do(a) {chave}: "))

print('\nMedidas resgitradas:')
for chave,valor in medidas.items():
    print(f'{chave.capitalize()}: {valor} cm\n')

medidas2 = {
            'torax':'',
            'busto':'',
            'ombros':'',
            'cintura':'',
            'quadril':'',
            'gluteo':'',
            'coxa_d':'',
            'coxa_e':'',
            'panturrilha_d':'',
            'panturrilha_e':'',
            'braco_d':'',
            'braco_e':''
            
}
for chave2 in medidas2:
    medidas2[chave2]= float(input(f"Digite sua medida do(a) {chave2}: "))
print('\nMedidas resgitradas:')
for chave2, valor2 in medidas2.items():
    print(f'{chave2.capitalize()}: {valor2} cm')
print('\nResultado:\n')
for chave in medidas:
    comparacao= (medidas2[chave]-medidas[chave])
    if comparacao >0:
        print(f'A medida do {chave} aumentoou em {comparacao} cm')
    elif comparacao ==0:
        print(f'A medida {chave} não mudou.')
    else:
        print(f'A medida do {chave} diminuiu em {abs(comparacao)} cm')
        























