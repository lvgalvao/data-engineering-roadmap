from fastapi import FastAPI, Request, Response, Query, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional

app = FastAPI()

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

# Define function to generate HTML content from data
def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Info</title>
    </head>
    <body>
        <h1>User Info</h1>
        <ul>
            <li>Name: {name}</li>
            <li>Age: {age}</li>
            <li>Email: {email}</li>
        </ul>
    </body>
    </html>
    """.format(**data)
    return html_content

# Define function to generate XML content from data
def generate_xml(data):
    xml_content = f"<user>\n" # noqa
    for key, value in data.items():
        xml_content += f"    <{key}>{value}</{key}>\n"
    xml_content += "</user>"
    return xml_content

# Define endpoint to handle content negotiation for Accept and query
# Define endpoint to handle content negotiation for Accept and query
@app.get("/user", responses={
    200: {"description": "User information", "content": {
        "application/json": {},
        "text/html": {},
        "application/xml": {}
    }}
})
async def get_user(request: Request, format: Optional[str] = Query(None, pattern="^(json|html|xml)$")):
    # Check if query parameter is present
    if format:
        if format == "json":
            return JSONResponse(content=data)
        elif format == "html":
            return HTMLResponse(content=generate_html(data))
        elif format == "xml":
            return Response(content=generate_xml(data), media_type="application/xml")

    # Check client's preferred content type from Accept header
    accept_header = request.headers.get("Accept")
    
    # Default to JSON if Accept header is not provided
    if not accept_header:
        return JSONResponse(content=data)
    
    # Parse Accept header to determine client's preferred content type
    if "application/json" in accept_header:
        return JSONResponse(content=data)
    elif "text/html" in accept_header:
        return HTMLResponse(content=generate_html(data))
    elif "application/xml" in accept_header:
        return Response(content=generate_xml(data), media_type="application/xml")
    else:
        # If no matching content type is found, return a 406 Not Acceptable response
        return Response(status_code=406, content="406 Not Acceptable: Unsupported Media Type")

# Define endpoint to handle content negotiation for file extension
@app.get("/user.{format}")
async def get_user_by_extension(format: str):
    """
    Retorna informações do usuário no formato especificado.

    Parâmetros:
    - format: Formato desejado da resposta. Opções disponíveis: json, html, xml.
    """
    if format == "json":
        return JSONResponse(content=data)
    elif format == "html":
        return HTMLResponse(content=generate_html(data))
    elif format == "xml":
        return Response(content=generate_xml(data), media_type="application/xml")
    else:
        raise HTTPException(status_code=406, detail="Unsupported Media Type")
    
@app.get("/users")
async def get_user_by_extension_final(format: str = None):
    if format == "json":
        return JSONResponse(content=data)
    elif format == "html":
        return HTMLResponse(content=generate_html(data))
    elif format == "xml":
        return Response(content=generate_xml(data), media_type="application/xml")
    else:
        raise HTTPException(status_code=406, detail="Unsupported Media Type")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
