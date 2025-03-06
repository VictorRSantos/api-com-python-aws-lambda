from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
    "users":[
        {"name":"usuario1", "phone":"111111111"},
        {"name":"usuario2", "phone":"222222222"},
        {"name":"usuario3", "phone":"333333333"},
    ]
}

companies ={
    "companies":[
        {"name":"empresa1", "telefone":"111111111"},
        {"name":"empresa2", "telefone":"222222222"},
        {"name":"empresa3", "telefone":"333333333"}
    ]
}


@app.route('/consumers/person', methods=['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response


@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response


@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} excluido com sucesso!"
    }
    return response


@app.route('/consumers/persons', methods=['GET'])
def get_person():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response


@app.route('/consumers/person/{id}', methods=['GET'])
def get_person(id):
    response = {
        "statusCode": 200,
        "body": { id: {"name":"usuario1", "phone":"111111111"}}
    }
    return response



# COMPANY
@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response


@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response


@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} excluida com sucesso!"
    }
    return response


@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response


@app.route('/consumers/company/{id}', methods=['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        "body": { id: {"name":"empresa1", "telefone":"111111111"} }
    }
    return response





