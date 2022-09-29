import random

vetor = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]

print('VAMOS JOGAR 21!')

def jogo_de_21():

    
    while True:
        a = vetor.pop(random.randrange(len(vetor)))
        b = vetor.pop(random.randrange(len(vetor)))
        
        x = vetor.pop(random.randrange(len(vetor)))
        y = vetor.pop(random.randrange(len(vetor)))
        
        total_jogador = a + b
        total_mesa = x + y
        
        print(f'Cartas da mesa {x}, {y} total de {total_mesa}.')
        print(f'Suas cartas {a}, {b} total de {total_jogador}.')
        
        while True:    
            s = str(input('mais uma carta? [S/N] ')).upper()[0]
            if s == 'S':
                carta_mesa = vetor.pop(random.randrange(len(vetor)))
                carta_jogar = vetor.pop(random.randrange(len(vetor)))
                
                total_jogador = total_jogador + carta_jogar
                total_mesa = total_mesa + carta_mesa
                
                print(f'Seu total é {total_jogador}.')
                print(f'O total da mesa é {total_mesa}.')
                
                if total_jogador == 21:
                    print('jogador venceu!\n')
                    break
                
                elif total_mesa == 21:
                    print('mesa venceu!\n')
                    break
                
                elif total_jogador > 21 or total_mesa > 21:
                    if total_jogador < total_mesa:
                        print('Jogador venceu!\n')
                        break
                    else:
                        print('Mesa Venceu\n')
                        break        
                
            elif s == 'N':
                
                if total_jogador > total_mesa:
                    print('Jogador venceu!\n')
                    break
                
                elif total_jogador < total_mesa:
                    print('Mesa venceu!\n')
                    break
                    
                else:
                    print('Empate!\n')
                    break          


jogo_de_21()