# Comandos
.PHONY: sih-download setup clean

info:
	@cat source/ascii-art.txt
	@echo "Desc: Software de análise de redes do grupo de pesquisa Gerotec."
	@echo "Autor: Matheus Ferreira"
	@echo "Universidade de Fortaleza, 2025."

# Configuração inicial, como instalação de dependências
setup:
	@echo "Instalando dependências do Python..."
	pip install -r requirements.txt

# Executa o script Python
sih-download:
	python source/sih-download.py

# Remove arquivos desnecessários ou temporários
clean:
	@echo "Limpando arquivos temporários..."
	rm -rf __pycache__ *.pyc