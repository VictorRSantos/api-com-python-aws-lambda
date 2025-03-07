from chalice import Chalice

app = Chalice(app_name='sales')

sales = {
    "sales":[
        {"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"},
        {"id":"2", "consumer":"usuário dois", "value":"11,00", "food":"estrogonofe"},
        {"id":"3", "consumer":"usuário três", "value":"12,50", "food":"macarronada"}
    ]
}

@app.route('/sales/offline', methods = ["POST"])
def create_sales():
    requests_params = app.current_request.json_body
    response ={
        "statusCode":200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response

@app.route('/sales/offline', methods = ["PUT"])
def update_sales():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response

@app.route('/sales/offline', methods = ["DELETE"])
def delete_sales():
    requests_params = app.current_request.json_body
    response = {
        "statusCode":200,
        "body": f"Venda {requests_params} exluida com sucesso!" 
    }
    return response

@app.route('/sales/offlines', methods = ["GET"])
def get_sales():
    response = {
        "statusCode":200,
        "body": sales        
    }
    return response

@app.route('/sales/offline/{id}', methods = ["GET"])
def get_sale(id):
    response = {
        "statusCode":200,
        "body": {id: {"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}}        
    }
    return response




@app.route('/sales/online', methods = ["POST"])
def create_sales():
    requests_params = app.current_request.json_body
    response ={
        "statusCode":200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response

@app.route('/sales/online', methods = ["PUT"])
def update_sales():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response

@app.route('/sales/online', methods = ["DELETE"])
def delete_sales():
    requests_params = app.current_request.json_body
    response = {
        "statusCode":200,
        "body": f"Venda {requests_params} exluida com sucesso!" 
    }
    return response

@app.route('/sales/online', methods = ["GET"])
def get_sales():
    response = {
        "statusCode":200,
        "body": sales        
    }
    return response

@app.route('/sales/online/{id}', methods = ["GET"])
def get_sale(id):
    response = {
        "statusCode":200,
        "body": {id: {"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}}        
    }
    return response