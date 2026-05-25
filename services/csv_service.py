import csv
from datetime import datetime

today = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')

def gerar_csv(parcelas, realstate):
    datas = [{'Month': i, 'Value': f'{(parcelas / 12 if i > 5 else (parcelas / 12) + 400):.2f}'} for i in range(1,13)]
    with open(f'data/Budget_{realstate}_{today}.csv', 'a', encoding='utf-8') as arq:
            writer = csv.DictWriter(arq, fieldnames=datas[0].keys())
            writer.writeheader()
            writer.writerows(datas)