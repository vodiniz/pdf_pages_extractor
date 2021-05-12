import os
from PyPDF2 import PdfFileWriter, PdfFileReader

def instructions():
    print('Esse programa irá pegar todos os documentos pdf da pasta em que ele se encontra e irá extrair as páginas escolhidas.')
    print('Para começar, Coloque todos os arquivos pdf na mesma pasta desse programa.')
    print('Agora renomeie os arquivos para 1.pdf 2.pdf...')
    print('O número será correspondente a ANP.')
    print('Aperte qualquer tecla para continuar o programa:')
    input()
    print('-------------------')
    return

def get_path():
    project_root = os.getcwd()
    return project_root

def get_file_name():
    file_list = []
    path = get_path()

    for file in os.listdir(path):
        if (file.endswith('.pdf')) and (os.path.isfile(os.path.join(path, file))):
            file_list.append(file)
    
    file_list = sorted(file_list)
    return file_list

def get_files_lenght():
    length = len([name for name in os.listdir('.') if os.path.isfile(name)])
    return length-1

def info_pages():
    print('Me fala a página/páginas que voce quer do pdf')
    print('Caso seja uma página apenas, escreva apenas o número.')
    print('Caso seja 2 ou mais páginas, coloque elas separadas por um -.')
    print('Exemplo páginas 4 a 6 --->  4-6')

    return

def get_needed_pages(pdf):
    print('----------------------')
    print('Estou extraindo as páginas do pdf: {}'.format(pdf))
    print('Quais páginas você quer ? \n')
    pages = input()
    split_pages = pages.split('-')

    if '-' in pages:
        page_start = int(split_pages[0])
        page_end = int(split_pages[1].replace('-',''))
        
        return page_start,page_end

    else:
        return int(pages), None

def start_extraction():
    pdf_number = get_files_lenght()
    base_name = input('Qual o ano ? Responda apenas com número: ')
    print('-------------------')
    base_name = base_name+'_Ano_ANP_'
    pdf_list = get_file_name()
    info_pages()

    for pdf in pdf_list:
        page_start, page_end = get_needed_pages(pdf)

        if page_end == None:
            inputPDF = PdfFileReader(open(pdf,'rb'))
            outputPDF = PdfFileWriter()
            outputPDF.addPage(inputPDF.getPage(page_start))
            with open ('{}{}'.format(base_name,pdf), 'wb') as outputStream:
                outputPDF.write(outputStream)

        else:
            inputPDF = PdfFileReader(open(pdf,'rb'))
            outputPDF = PdfFileWriter()
            while (page_start <= page_end):
                outputPDF.addPage(inputPDF.getPage(page_start))
                page_start = page_start + 1

            with open ('{}{}'.format(base_name,pdf), 'wb') as outputStream:
                    outputPDF.write(outputStream)

    return

def main():
    instructions()
    start_extraction()
    return


main()