from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse, HTMLResponse

import csv
from io import StringIO

app = FastAPI()

@app.get("/listar-csv")
def listar_csv():
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]] # Dados
    stream = StringIO() # Transforma um objeto em um arquivo
    csv.writer(stream).writerows(data) # Dessa forma escrevemos os "data" no formarto csv no stream
    return stream.getvalue()

@app.get("/download-csv/")
def download_csv():
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]] # Dados
    stream = StringIO() # Transforma um objeto em um arquivo
    csv.writer(stream).writerows(data) # Dessa forma escrevemos os "data" no formarto csv no stream
    return StreamingResponse(iter([stream.read()]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=report.csv"})

@app.get("/portal")
async def get_portal(teleport: bool = False):
    if teleport:
        return HTMLResponse(content="""
                            <html>
                                <head>
                                    <title>Some HTML in here</title>
                                </head>
                                <body>
                                    <h1>Look ma! HTML!</h1>
                                </body>
                            </html>""")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})