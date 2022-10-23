wget https://github.com/karinadyahpermatasari/karinadyper.github.io/blob/main/requirement.txt
pip install -r requirement.txt
import streamlit as st
st.write("Hello")
st.title("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.title("Analisis Perekonomian Indonesia")
st.markdown("Dua tahun terakhir ini, dunia tengah dihadapi berbagai permasalahan, seperti pandemi Covid-19, invasi Ukraina-Rusia, dan konflik China-Taiwan. Hal tersebut mampu menekan perekonomian hampir di seluruh dunia, termasuk Indonesia. Bagaimanakah keadaan perekonomian Indonesia sekarang?")

st.subheader("Pertumbuhan Ekonomi Indonesia")

#@title
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
bungaacuan=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/BI-7Day-RR.xlsx")
inflasi=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/InflasiM.xlsx")
bensin=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/Inflasidanbensin.xlsx")
pdb=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/PDBQ.xlsx")
ak=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/AK.xlsx")
ak2022=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/AK 2022 Feb.xlsx")
ak2021=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/AK 2021 Feb.xlsx")
pengeluaran=pd.read_excel("/content/drive/MyDrive/Colab Notebooks/TETRIS/Proporsi pengeluaran.xlsx")
pdb.astype({'Tahun':'datetime64[ns]'}).dtypes

#@title
fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(14,6))
ppdb=pdb.loc[0:13]
#plot GDP
time=ppdb['Tahun']
gdp=ppdb['PDB (Triliun Rupiah)']
ax.plot(time,gdp)
ax.set_title('PDB di Indonesia',fontsize=12)
ax.set_xlabel('Waktu')
ax.set_ylabel('PDB (Triliun Rupiah)')
ax.text(1,-0.1,'Sumber data: bps.go.id', color='blue',ha='right',transform=ax.transAxes)
#ax.text(0.95,0.85,'berlangsungnya pandemi Covid-19', color='red',ha='right',transform=ax.transAxes)
ax.grid(color='darkgray', linestyle=':', linewidth=0.5)

#@title
fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(14,6))
ppdb=pdb.loc[0:13]

time=inflasi['Tanggal']
inf=inflasi['Tingkat Inflasi']
ax.plot(time,inf)
ax.set_title('Tingkat Inflasi di Indonesia',fontsize=12)
ax.set_xlabel('Waktu')
ax.set_ylabel('Tingkat Inflasi (%)')
ax.text(1,-0.1,'Sumber data: bps.go.id', color='blue',ha='right',transform=ax.transAxes)
ax.text(0,-0.25,'catatan :\nSejak Jan-2020, IHK berdasarkan pola konsumsi dari Survei Biaya Hidup 2018 (2018=100) di 90 kota', color='red',ha='left',transform=ax.transAxes)
ax.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.tight_layout()
plt.show()

st.caption("Di Indonesia, pertumbuhan ekonomi dapat ditinjau dari data Produk Domestik Bruto (PDB) atas dasar harga konstan. Berdasarkan grafik PDB diatas, Indonesia terlihat mendapatkan tekanan ekonomi di tahun 2020. Hal ini bertepatan dengan terjadinya pandemi Covid-19. Menurut definisi, resesi merupakan pertumbuhan ekonomi secara negatif selama dua periode kuartal berurutan (Giuliani dan Massari, 2017). Pada tahun 2020, Indonesia telah mengalami resesi dimana terjadi penurunan nilai PDB sekitar 200000 M Rupiah. Pada waktu yang sama, tingkat inflasi Indonesia mengalami penurunan hinnga dibawah angka 2.5%. Setelah resesi, Indonesia mampu memperbaiki perekonomiannya hingga saat ini, dimana mengalami kenaikan nilai PDB hingga diatas 2800000 M Rupiah. Hal ini juga diiringi dengan kenaikan tingkat inflasi yang cukup tinggi hingga mencapai angka 5%. Berdasarkan kedua grafik diatas, saat ini Indonesia terlihat mampu bangkit dari tekanan ekonomi terlepas dari potensi-potensi geopolitik yang terjadi dimasa mendatang.")

st.subheader("Daftar Pustaka")
st.caption("Giuliani, M., & Massari, S. A. (2019). The economic vote at the party level: Electoral behaviour during the Great Recession. Party Politics, 25(3), 461–473. https://doi.org/10.1177/1354068817728214")

#@title
bunga=bungaacuan.sort_index(ascending=0)
# Bar chart with time against interest
plt.bar(bunga.iloc[42:45]['Tanggal'], bunga.iloc[42:45]['BI-7Day-RR'])
 
plt.title("Bunga Acuan")
 
# Setting the X and Y labels
plt.xlabel('Tanggal')
plt.ylabel('Bunga Acuan')
 
# Adding the legends
plt.show()

#@title
# Bar chart with time against interest
plt.bar(ak['Waktu'], ak['Upah'])
 
plt.title("Upah Kerja")
 
# Setting the X and Y labels
plt.xlabel('Waktu')
plt.ylabel('Upah (Ribu Rp)')
 
# Adding the legends
plt.show()

#@title
fig, ax=plt.subplots(1,2,figsize=(10,10))
#Creating the pie chart
ax[1].pie(ak2022['Jumlah'], labels = ak2022['Angkatan Kerja'],autopct='%1.1f%%',colors = ['#7B68EE','#483D8B'])
ax[0].pie(ak2021['Jumlah'], labels = ak2021['Angkatan Kerja'],autopct='%1.1f%%',colors = ['#7B68EE','#483D8B'])
#Adding the aesthetics
ax[1].set_title('Angkatan Kerja 2022')
ax[0].set_title('Angkatan Kerja 2021')
#Show the plot
plt.show()


#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(pengeluaran['Waktu']), y=list(pengeluaran['Konsumsi'])))

# Set title
fig.update_layout(
    title_text="Proporsi Konsumsi terhadap Pengeluaran",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(pengeluaran['Waktu']), y=list(pengeluaran['Cicilan'])))

# Set title
fig.update_layout(
    title_text="Proporsi Cicilan terhadap Pengeluaran",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()


#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(pengeluaran['Waktu']), y=list(pengeluaran['Tabungan'])))

# Set title
fig.update_layout(
    title_text="Proporsi Tabungan terhadap Pengeluaran",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(pengeluaran['Waktu']), y=list(pengeluaran['Cicilan'])))
fig.add_trace(
    px.Scatter(x=list(pengeluaran['Waktu']), y=list(pengeluaran['Tabungan'])))

# Set title
fig.update_layout(
    title_text="Proporsi Cicilan terhadap Pengeluaran",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(bensin['Tanggal']), y=list(bensin['Tingkat Inflasi'])))


# Set title
fig.update_layout(
    title_text="Tingkat Inflasi",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

fig.update_layout(
    annotations=[
        dict(
            x="2022-09-03",
            y=0,
            arrowcolor="rgba(63, 81, 181, 0.2)",
            arrowsize=0.3,
            ax=0,
            ay=30,
            text="state1",
            xref="x",
            yanchor="bottom",
            yref="y"
        )]
)
fig.update_layout(
    shapes=[
        dict(
            fillcolor="rgba(63, 81, 181, 0.2)",
            line={"width": 0},
            type="rect",
            x0="2022-09-03",
            x1="2022-10-01",
            xref="x",
            y0=0,
            y1=0.95,
            yref="paper"
        )])


# Create figure
fig = px.Figure()

# Add traces
fig.add_trace(px.Scatter(
    x=list(pengeluaran['Waktu']),
    y=list(pengeluaran['Konsumsi']),
    name="Konsumsi",
    text=["8", "3", "2", "10", "5", "5", "6", "8", "3", "3", "7", "5", "10", "10", "9",
          "14"],
    yaxis="y",
))


fig.add_trace(px.Scatter(
    x=list(pengeluaran['Waktu']),
    y=list(pengeluaran['Cicilan']),
    name="Cicilan",
    text=["53.0", "69.0", "89.0", "41.0", "41.0"],
    yaxis="y2",
))

fig.add_trace(px.Scatter(
    x=list(pengeluaran['Waktu']),
    y=list(pengeluaran['Tabungan']),
    name="Tabungan",
    text=["9.6", "4.6", "2.7", "8.3", "18", "7.3", "3", "7.5", "1.0", "0.5", "2.8",
          "9.2",
          "13", "5.8", "6.9"],
    yaxis="y3",
))


# style all the traces
fig.update_traces(
    hoverinfo="name+x+text",
    line={"width": 0.5},
    marker={"size": 8},
    mode="lines+markers",
    showlegend=False
)


# Update axes
fig.update_layout(
    xaxis=dict(
        autorange=True,
        range=["2018-10-31 18:36:37.3129", "2022-09-30 05:23:22.6871"],
        rangeslider=dict(
            autorange=True,
            range=["2018-10-31 18:36:37.3129", "2022-09-30 05:23:22.6871"]
        ),
        type="date"
    ),
    yaxis=dict(
        anchor="x",
        autorange=True,
        domain=[0, 0.2],
        linecolor="#673ab7",
        mirror=True,
        range=[-60.0858369099, 28.4406294707],
        showline=True,
        side="right",
        tickfont={"color": "#673ab7"},
        tickmode="auto",
        ticks="",
        title="Konsumsi (%)",
        titlefont={"color": "#673ab7"},
        type="linear",
        zeroline=False
    ),
    yaxis2=dict(
        anchor="x",
        autorange=True,
        domain=[0.2, 0.4],
        linecolor="#E91E63",
        mirror=True,
        range=[29.3787777032, 100.621222297],
        showline=True,
        side="right",
        tickfont={"color": "#E91E63"},
        tickmode="auto",
        ticks="",
        title="Cicilan (%)",
        titlefont={"color": "#E91E63"},
        type="linear",
        zeroline=False
    ),
    yaxis3=dict(
        anchor="x",
        autorange=True,
        domain=[0.4, 0.6],
        linecolor="#795548",
        mirror=True,
        range=[-3.73690396239, 22.2369039624],
        showline=True,
        side="right",
        tickfont={"color": "#795548"},
        tickmode="auto",
        ticks="",
        title="Tabungan (%)",
        titlefont={"color": "#795548"},
        type="linear",
        zeroline=False
    )
)

# Update layout
fig.update_layout(
#    title_text="Proporsi Cicilan terhadap Pengeluaran",xaxis_title='Waktu',
    dragmode="zoom",
    hovermode="x",
    legend=dict(traceorder="reversed"),
    height=900,
    template="plotly_white",
    margin=dict(
        t=100,
        b=100
    ),
)
# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

#@title
import plotly.graph_objects as px

fig = px.Figure()

fig.add_trace(
    px.Scatter(x=list(bensin['Tanggal']), y=list(bensin['Tingkat Inflasi'])))


# Set title
fig.update_layout(
    title_text="Tingkat Inflasi",xaxis_title='Waktu',
                   yaxis_title='Persentase (%)'
)
fig.update_layout(
    annotations=[
        dict(
            x="2022-09-03",
            y=0,
            arrowcolor="rgba(63, 81, 181, 0.2)",
            arrowsize=0.3,
            ax=0,
            ay=30,
            text="I",
            xref="x",
            yanchor="bottom",
            yref="y"
        ),
        dict(
            x="2022-04-01",
            y=0,
            arrowcolor="rgba(76, 175, 80, 0.1)",
            ax=0,
            ay=30,
            text="II",
            xref="x",
            yanchor="bottom",
            yref="y"
        ),
        dict(
            x="2018-10-10",
            y=0,
            arrowcolor="rgba(89, 269, 181, 0.2)",
            ax=0,
            ay=30,
            text="III",
            xref="x",
            yanchor="bottom",
            yref="y")]
)

fig.update_layout(
    shapes=[
        dict(
            fillcolor="rgba(63, 81, 181, 0.2)",
            line={"width": 0},
            type="rect",
            x0="2022-09-03",
            x1="2022-10-01",
            xref="x",
            y0=0,
            y1=0.95,
            yref="paper"
        ),
        dict(
            fillcolor="rgba(76, 175, 80, 0.1)",
            line={"width": 0},
            type="rect",
            x0="2022-04-01",
            x1="2022-10-01",
            xref="x",
            y0=0,
            y1=0.95,
            yref="paper"
        ),
        dict(
            fillcolor="rgba(89, 269, 181, 0.2)",
            line={"width": 0},
            type="rect",
            x0="2018-10-10",
            x1="2022-10-01",
            xref="x",
            y0=0,
            y1=0.95,
            yref="paper")])

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

