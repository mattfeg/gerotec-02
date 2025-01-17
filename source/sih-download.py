from pysus import SIH
from pysus.ftp import FTPSingleton

FTPSingleton.timeout = 180
print("Carregando arquivos do SIH...")
sih = SIH().load()
print("Arquivos do SIH carregados!")

files = sih.get_files("RD", uf="CE",
year=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
month=[1,2,3,4,5,6,7,8,9,10,11,12])

print("Baixando arquivos do SIH...")
arquivos = sih.download(files,local_dir="./dados/DBC")
print("Arquivos do SIH baixados!")
