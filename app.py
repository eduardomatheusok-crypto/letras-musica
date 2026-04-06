import streamlit as st
import requests
from googletrans import Translator

translator = Translator()
GENIUS_TOKEN = "6ghphiCytqSOwUYOrkBP5S-Er4TBSh2TPWnMjhYb03EN1L328W1tIDNVDWUcT7BV"

st.title("🎵 Letras de Música e Informações do Artista 🎶")

banda = st.text_input("Digite o nome da banda:", key="banda")
musica = st.text_input("Digite o nome da música:", key="musica")
pesquisar = st.button("Pesquisar")

if "letra" not in st.session_state:
    st.session_state.letra = ""
if "letra_traduzida" not in st.session_state:
    st.session_state.letra_traduzida = ""

def pesquisar_letra(musica, banda):
    url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados.get("lyrics", "")
    else:
        return ""

def buscar_artista_genius(artista, token):
    url = f"https://api.genius.com/search?q={artista}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        dados = response.json()
        hits = dados["response"]["hits"]
        if hits:
            artista_info = hits[0]["result"]["primary_artist"]
            return {
                "nome": artista_info["name"],
                "url": artista_info["url"],
                "imagem": artista_info["image_url"]
            }
    return None

if pesquisar:
    st.session_state.letra = pesquisar_letra(musica, banda)
    info_artista = buscar_artista_genius(banda, GENIUS_TOKEN)

if st.session_state.letra:
    st.success("Música Encontrada")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.text_area("Letra Original:", st.session_state.letra, height=300)
    
    with col2:
        if info_artista:
            st.subheader(info_artista["nome"])
            st.image(info_artista["imagem"], width=200)
            st.markdown(f"[Mais sobre {info_artista['nome']}]({info_artista['url']})")
    
    idioma_destino = st.selectbox(
        "Escolha o idioma de tradução:",
        options=["pt", "es", "fr", "de", "it", "en"],
        index=0
    )

    if st.button("Traduzir"):
        st.session_state.letra_traduzida = translator.translate(
            st.session_state.letra, src='en', dest=idioma_destino
        ).text

    if st.session_state.letra_traduzida:
        st.text_area(f"Letra Traduzida ({idioma_destino}):", st.session_state.letra_traduzida, height=300)
else:
    if pesquisar:
        st.error("Infelizmente não foi possível achar a letra")