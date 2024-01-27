### Instalação e Configuração
1. Clone o repositório:
```bash
git clone https://github.com/lvgalvao/Workshop-aberto-aovivo
cd Workshop-aberto-aovivo
```
2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Instale as dependências do projeto:
```bash
python -m venv .venv
# O padrao é utilizar .venv
source .venv/bin/activate
# Usuários Linux e mac
.venv\Scripts\Activate
# Usuários Windows
pip install -r requirements.txt  
```