import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Leer y procesar los datos
data_file = 'facturas.csv'
df = pd.read_csv(data_file)

total_facturas = df['Cantidad facturas'].sum()
df['Porcentaje'] = (df['Cantidad facturas'] / total_facturas) * 100

df_filtrado = df[df['Porcentaje'] > 10]

pie_chart = px.pie(df_filtrado, values='Porcentaje', names='Proveedor', title='Proveedores con más del 10% de facturas')
bar_chart = px.bar(df, x='Cantidad facturas', y='Proveedor', orientation='h', title='Distribución de facturas por proveedor')

df_ranking = df.sort_values(by='Cantidad facturas', ascending=False)
df_ranking['Ranking'] = range(1, len(df_ranking) + 1)

ranking_chart = px.bar(df_ranking, x='Cantidad facturas', y='Proveedor', orientation='h', title='Ranking de proveedores por cantidad de facturas')
ranking_chart.update_yaxes(categoryorder='total ascending')

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    html.H1('Análisis de Facturas por Proveedor'),
    dcc.Graph(figure=pie_chart, id='pie-chart'),
    dcc.Graph(figure=bar_chart, id='bar-chart'),
    dcc.Graph(figure=ranking_chart, id='ranking-chart')
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
