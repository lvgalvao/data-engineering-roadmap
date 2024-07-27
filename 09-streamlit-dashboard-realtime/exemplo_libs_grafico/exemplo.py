import folium
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_folium import folium_static
from wordcloud import WordCloud

# Exemplo de gráfico Matplotlib
st.header("Gráfico Matplotlib")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
st.pyplot(fig)

# Exemplo de mapa Folium
st.header("Mapa Folium")
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.Marker([45.5236, -122.6750], popup="The Waterfront").add_to(m)
folium_static(m)

# Exemplo de nuvem de palavras WordCloud
st.header("Nuvem de Palavras")
text = "Python Streamlit Matplotlib Folium WordCloud"
wordcloud = WordCloud(
    width=800, height=400, background_color="white"
).generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
