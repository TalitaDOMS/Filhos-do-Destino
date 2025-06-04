from flask import Flask, render_template, redirect
from openpyxl import Workbook, load_workbook
from random import random
import os

app = Flask(__name__)
ARQUIVO = 'fichas.xlsx'

def criarPersonagem(nome):
    wb = load_workbook(ARQUIVO)
    wb.create_sheet(title=nome)
    wb.save(ARQUIVO)

if not os.path.exists(ARQUIVO):
    wb = Workbook()
    wb.title = 'Resumo do RPG'
    ws = wb.active
    ws.append(['Mestre','Inicio da campanha'])
    ws.append(['Talita DOMS', '08/06/2025'])
    wb.save(ARQUIVO)

criarPersonagem('Bah')
wb = load_workbook(ARQUIVO)
ws = wb['Bah']
wb.save(ARQUIVO)

@app.route('/')
def teste():
    wb = load_workbook(ARQUIVO)
    ws = wb.active
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)