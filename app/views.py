from flask import Flask, request, jsonify
from graphene import Schema
from app.product_schema import Query, Mutation

# Create Flask app
app = Flask(__name__)

# GraphQL endpoint
@app.route('/graphql', methods=['POST'])
def graphql():
    # Get request data
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables')

    # Execute GraphQL query
    result = Schema(query=Query, mutation=Mutation).execute(query, variables=variables)

    # Return GraphQL response
    return jsonify(result.data), 200

if __name__ == '__main__':
    app.run(debug=True)