from flask_restful import Resource
from flask_restful import reqparse

class HelloResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade', type=str, required=True, help='O campo idade é obrigatorio')

    def get(self, nome):
        message = f'Hello {nome}'
        return {"message": message}

    def post(self, nome):
        data = HelloResource.parser.parse_args()
        idade = data['idade']
        return {"message": f'Olá {nome} você informou que tem {idade} anos'}