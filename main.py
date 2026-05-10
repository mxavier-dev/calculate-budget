from models.realstates import *
from services.csv_service import *

valor_contrato = 2000
parcelas = valor_contrato / 5

try:
    while True:
        print('--- Calculadora de orçamentos - Imobiliaria R.M ---')
        print('\nOpções de Imóveis disponíveis:\n'
              '1 - Apartamento\n'
              '2 - Casa\n'
              '3 - Estudio\n'
              '0 - Sair')
        escolha1 = input('Escolha uma das opções acima: ')
        if escolha1 == '1':
            print('\n==== Você escolheu apartamento ====\n')
            print('Número de quartos:\nMínimo: 1 quarto\nMáximo: 2 quartos\n')
            if (quartos := int(input('Digite o número de quartos que deseja: '))) not in [1,2]:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            if (garagem := input('Precisa de vaga na garagem? (S | N): ').upper()) in ['S','N']:
                garagem = (True if garagem == 'S' else False)
            else:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            if (crianca := input('Você tem criança? (S | N): ').upper()) in ['S','N']:
                crianca = (True if crianca == 'S' else False)
            else:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            apartamento = Apartment(rooms=quartos, garage=garagem, kids=crianca)
            aluguel = apartamento.calculate_budget()
            print('\n===== ORÇAMENTO ====='
                  '\nImóvel: Apartamento\n'
                  f'Quartos: {quartos}\n'
                  f'Garagem: {"Sim" if garagem else "Não"}\n'
                  f'\nOrçamento Total: {aluguel}\n'
                  f'Valor por mês: 12x de R$ {aluguel / 12:.2f}\n'
                  f'\nContrato:\n5x de R$ {parcelas}')
            gerar_csv(aluguel, 'Apartment')
            break
        elif escolha1 == '2':
            print('\n==== Você escolheu Casa ====\n')
            print('Número de quartos:\nMínimo: 1 quarto\nMáximo: 2 quartos\n')
            if (quartos := int(input('Digite o número de quartos que deseja: '))) not in [1,2]:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            if (garagem := input('Precisa de vaga na garagem? (S | N): ').upper()) in ['S','N']:
                garagem = (True if garagem == 'S' else False)
            else:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            casa = House(rooms=quartos, garage=garagem)
            aluguel = casa.calculate_budget()
            print('\n===== ORÇAMENTO ====='
                  '\nImóvel: Casa\n'
                  f'Quartos: {quartos}\n'
                  f'Garagem: {"Sim" if garagem else "Não"}\n'
                  f'\nOrçamento Total: {aluguel}\n'
                  f'Valor por mês: 12x de R$ {aluguel / 12:.2f}\n'
                  f'\nContrato:\n5x de R$ {parcelas}')
            gerar_csv(aluguel, 'House')
            break
        elif escolha1 == '3':
            print('\n==== Você escolheu Estudio ====\n')
            qtnd_vagas = 0
            if (garagem := input('Precisa de vaga na garagem? (S | N): ').upper()) in ['S','N']:
                garagem = (True if garagem == 'S' else False)
            else:
                print(f'\n{"="*30} Digite apenas opções corretas {"="*30}\n')
                continue
            if garagem:
                vagas = input('\nVocê tem direito a 2 vagas na garagem, gostaria de ter mais? (S | N): ').upper()
                qtnd_vagas += (2 if vagas == 'N' else (int(input('Então, quantas vagas adicionais deseja: '))+2))
            estudio = Studio(garage_spaces=qtnd_vagas)
            aluguel = estudio.calculate_budget()
            print('\n===== ORÇAMENTO ====='
                  '\nImóvel: Estudio\n'
                  f'Garagem: {"Sim" if garagem else "Não"}\n'
                  f'Vagas na garagem: {qtnd_vagas}\n'
                  f'\nOrçamento Total: {aluguel}\n'
                  f'Valor por mês: 12x de R$ {aluguel / 12:.2f}\n'
                  f'\nContrato:\n5x de R$ {parcelas}')
            gerar_csv(aluguel, 'Studio')
            break
        elif escolha1 == '0':
            print('\n===== Fim do programa =====')
            break
        else:
            print(f'\n{"="*20} Escolha uma opção válida {"="*20}\n')
            continue
except ValueError:
    print(f'\n{"=" * 30} Digite apenas opções corretas {"=" * 30}\n')