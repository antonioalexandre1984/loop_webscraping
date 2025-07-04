from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configura navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa em segundo plano
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessa a página
url = 'https://loopbrasil.net/lotes/?&cate[]=3'
driver.get(url)

# Espera os cards aparecerem (com timeout de 15s)
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'section#lote'))
    )
    print("🟢 Cards carregados com sucesso")
except:
    print("❌ Timeout ao esperar pelos cards")
    driver.quit()
    exit()

time.sleep(2)  # espera adicional

cards = driver.find_elements(By.CSS_SELECTOR, 'section#lote')
print(f"🔢 Total de cards encontrados: {len(cards)}")

dados = []

for idx, card in enumerate(cards, 1):
    print(f"\n🔎 Processando card #{idx}")
    time.sleep(1)  # evita bloqueio por scraping agressivo

    def safe_find(selector, many=False, attr=None):
        try:
            el = card.find_elements(By.CSS_SELECTOR, selector) if many else card.find_element(By.CSS_SELECTOR, selector)
            return el if attr is None else el.get_attribute(attr)
        except:
            return '' if not many else []

    titulo = safe_find('.carname')
    print(f"✔️ Título: {titulo}")

    lances = safe_find('.LL_count_lances')
    print(f"✔️ Lances: {lances}")

    views = safe_find('.LL_count')
    print(f"✔️ Visualizações: {views}")

    data_e_horario = safe_find('.coluna .cor_969696', many=True)
    data_leilao = data_e_horario[0].text.strip() if len(data_e_horario) > 0 else ''
    horario = data_e_horario[1].text.strip() if len(data_e_horario) > 1 else ''
    print(f"✔️ Data: {data_leilao} | Horário: {horario}")

    lance_atual = safe_find('.LL_lance_atual')
    print(f"✔️ Lance Atual: {lance_atual}")

    situacao = safe_find('.LL_situacao li p')
    print(f"✔️ Situação: {situacao}")

    link = safe_find('a.card', attr='href')
    print(f"✔️ Link: {link}")

    imagem = safe_find('.img img', attr='src')
    print(f"✔️ Imagem: {imagem}")

    dados.append({
        'titulo': titulo,
        'lances': lances,
        'visualizacoes': views,
        'data_leilao': data_leilao,
        'horario': horario,
        'lance_atual': lance_atual,
        'situacao': situacao,
        'link': f'https://loopbrasil.net{link}' if link.startswith('/') else link,
        'imagem': f'https://loopbrasil.net{imagem}' if imagem.startswith('/') else imagem,
    })

driver.quit()

# Exporta para CSV
df = pd.DataFrame(dados)
df.to_csv('export.csv', index=False, encoding='utf-8')
print("\n📁 Dados exportados com sucesso para 'export.csv'")
