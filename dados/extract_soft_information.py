import pandas as pd
import argparse
import os.path

def verifica_arquivo_existe(parser, arg):
    if not os.path.exists(arg):
        parser.error("O arquivo  %s não existe!" % arg)
    else:
        return open(arg, 'r')  # retorna o handle do arquivo aberto

def main():
   parser = argparse.ArgumentParser(description='Extrai as informações soft do cliente')
   parser.add_argument("-i", dest="arqCsvFull", required=True,
                    help="arquivo com todas as informações do cliente", metavar="ArquivoCSVFull",
                    type=lambda x: verifica_arquivo_existe(parser, x))
   parser.add_argument("-o", dest="arqCsvSoft", required=True,
                    help="arquivo com resultado das informações soft do cliente", metavar="ArquivoCSVSoft")
   args = parser.parse_args()
   
   data = pd.read_csv(args.arqCsvFull)
   df = pd.DataFrame(data, columns= ['Unnamed: 0','addr_state','annual_inc','emp_length','home_ownership','verification_status','loan_status'])
   df.rename(columns = {'Unnamed: 0':'borrower_id'}, inplace = True)
   #print (df)
   df.to_csv(args.arqCsvSoft, mode='w', sep=',', header=True, index=False, encoding='utf-8-sig')
   

if __name__ == "__main__":
   main()
