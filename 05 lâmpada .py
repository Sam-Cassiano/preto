def descobrir_lampadas():
    # Estado inicial dos interruptores e lâmpadas
    interruptor_1 = False
    interruptor_2 = False
    interruptor_3 = False
    
    # Estado inicial das lâmpadas (todas estão desligadas e frias)
    lampada_1 = {'ligada': False, 'quente': False}
    lampada_2 = {'ligada': False, 'quente': False}
    lampada_3 = {'ligada': False, 'quente': False}
    
    # 1º Passo: Ligue o Interruptor 1 por 5 minutos
    interruptor_1 = True
    lampada_1['ligada'] = True
    lampada_1['quente'] = True  # Depois de 5 minutos, a lâmpada aquece
    
    # 2º Passo: Desligue o Interruptor 1 e ligue o Interruptor 2
    interruptor_1 = False
    lampada_1['ligada'] = False  # Desligada, mas ainda está quente
    interruptor_2 = True
    lampada_2['ligada'] = True
    
    # Agora, vamos "ir até a sala das lâmpadas" para verificar os estados
    print("Vá até a sala das lâmpadas...")

    # 3º Passo: Verificar o estado das lâmpadas
    if lampada_2['ligada']:
        print("A lâmpada 2 está acesa -> Controlada pelo Interruptor 2.")
    if not lampada_1['ligada'] and lampada_1['quente']:
        print("A lâmpada 1 está apagada, mas quente -> Controlada pelo Interruptor 1.")
    if not lampada_3['ligada'] and not lampada_3['quente']:
        print("A lâmpada 3 está apagada e fria -> Controlada pelo Interruptor 3.")

# Executar a simulação
descobrir_lampadas()
