# 🎵 Aplicação de Letras de Música

## 📖 Descrição
Aplicativo em **Python com Streamlit** que permite buscar letras de músicas, traduzir para diversos idiomas e visualizar informações sobre o artista de forma simples e interativa.  

O projeto demonstra habilidades em **consumo de APIs, manipulação de dados e criação de interfaces web**.

---

## ✨ Funcionalidades
- 🔍 **Busca de letras** usando a API [Lyrics.ovh](https://lyrics.ovh/)  
- 🌐 **Tradução de letras** para diferentes idiomas com [Googletrans](https://pypi.org/project/googletrans/)  
- 🎤 **Informações do artista** via [Genius API](https://genius.com/developers)  
- 🖥️ **Interface limpa e interativa** usando Streamlit  

---

## 🛠 Tecnologias utilizadas
- Python 3.x  
- [Streamlit](https://streamlit.io/)  
- [Requests](https://pypi.org/project/requests/) (para consumir APIs)  
- [Googletrans](https://pypi.org/project/googletrans/) (tradução automática)  
- [Genius API](https://genius.com/developers) (informações do artista)  

---

## 🚀 Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/letras-musica.git
Entre na pasta do projeto:
cd letras-musica
Instale as dependências:
pip install -r requirements.txt
Execute o aplicativo:
streamlit run app.py
Abra o navegador no endereço exibido pelo Streamlit (geralmente http://localhost:8501)
