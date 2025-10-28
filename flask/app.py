from flask    import Flask, request, send_file
from utils    import *

import  pandas as pd
import  io
import  os

URL_API        = os.getenv("HOSTAPI")
app            = Flask(__name__)
app.secret_key = 'gcNCbQCEn4AjOHIjFKzk8ZVbfhUsE3GRE7rH6scugcHlEaLw1knLcNS5tv+sexaMSu5wEKFhe15vJLsfY78jbA=='
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(__name__)

def calcula_ispt(dataF, api):
    dfi = carga_tabla_ispt(api)
    dataF['sueldo_mensual']   = dataF['sueldo_mensual'].astype(float) 
    dataF['impuesto'] = dataF['impuesto'].astype(float) 
    for i in dataF.index:
        sueldo   = dataF.loc[i,'sueldo_mensual'] 
        impuesto = ispt(dfi, sueldo)
        dataF.loc[i,'impuesto'] = round(impuesto,2)
    dfr = dataF
    return dfr

@app.route('/upload', methods=['POST'])
def procesar_csv():
    print(request.files)
    if 'archivo_csv' not in request.files:
        return {'error': 'No se encontro el archivo'}, 400
    
    archivo = request.files['archivo_csv']
    try:
        df = pd.read_csv(archivo)
    except Exception as e:
        return {'error': f'Error al leer CSV: {str(e)}'}, 400

    
    df = calcula_ispt(df, URL_API)

    # Preparar respuesta
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='procesado.csv'
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", debug = True)
