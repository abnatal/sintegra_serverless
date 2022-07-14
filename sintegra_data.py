from bs4 import BeautifulSoup

HTML_FIELDS = ('data_consulta', 'cnpj', 'ie', 'estado', 'razao_social', 'logradouro', 'numero', 'complemento', 'bairro', 'uf', 'cidade', 'cep', 'email', 'telefone', 'atividade', 'data_ie', 'situacao', 'data_situacao', 'observacao', 'regime_icms')

def extract_data(html):
    result = {}
    soup = BeautifulSoup(html, "html.parser")
    dados = soup.findAll('td', {'class':'td-conteudotwo'})
    for i, dado in enumerate(dados):
        if i < len(HTML_FIELDS):
            result[HTML_FIELDS[i]] = dado.text.strip().strip('\t').strip('\n')
    return result