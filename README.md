# 🔍 Leilão Scraper - LoopBrasil

Este projeto realiza o web scraping do site [Loop Brasil Leilões](https://loopbrasil.net/lotes/?&cate[]=3), extraindo informações de **lotes de veículos** usando **Selenium** com navegador headless em um **container Docker**.

Os dados extraídos são exportados em um arquivo `export.csv`.

---

## 📦 Tecnologias utilizadas

- Python 3.11
- Selenium WebDriver
- WebDriverManager (automatiza o download do ChromeDriver)
- Chromium (navegador headless no Docker)
- Docker
- Pandas (para exportar CSV)

---

## 🏁 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/leilao-scraper.git
cd leilao-scraper
2. Construa a imagem Docker
bash
Copiar
Editar
docker build -t leilao-scraper .
3. Execute o scraper
bash
Copiar
Editar
docker run --rm -v $(pwd):/app leilao-scraper
📁 Um arquivo chamado export.csv será gerado na raiz do projeto com os dados dos lotes.

📄 Estrutura esperada no CSV
Campo	Descrição
titulo	Nome do veículo do lote
lances	Quantidade de lances recebidos
visualizacoes	Quantidade de visualizações
data_leilao	Data programada para o leilão
horario	Horário do leilão
lance_atual	Valor atual do maior lance
situacao	Situação do lote (ex: "Aberto")
link	Link direto para o lote
imagem	URL da imagem do veículo

🛠 Dependências (caso use fora do Docker)
Se quiser rodar localmente sem Docker:

bash
Copiar
Editar
pip install -r requirements.txt
python scraper.py
🧩 Observações
O scraper usa WebDriverWait para garantir que os elementos sejam carregados antes da extração.

Um pequeno sleep() entre os cards evita bloqueios por scraping agressivo.

O navegador roda em modo headless (sem abrir interface gráfica).


---

Se quiser, posso empacotar esse `README.md` junto com o restante dos arquivos (`scraper.py`, `Dockerfile`, etc.) em um `.zip`. Deseja que eu gere isso agora?

