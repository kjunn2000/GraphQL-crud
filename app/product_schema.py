import graphene

# Define GraphQL types
class ProductType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()

# Define the query type
class Query(graphene.ObjectType):
    product = graphene.Field(ProductType, name=graphene.String(required=True))

    def resolve_product(self, info, name):
        # Resolver function to search for a product by name
        # This is where you would typically query your database
        # For demonstration purposes, let's return a dummy product
        return {'id': 1, 'name': name, 'description': 'Sample product description', 'price': 10.99}

# Define the mutation type
class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, description, price):
        # Resolver function to create a new product
        # This is where you would typically create a new product in your database
        # For demonstration purposes, let's return the created product
        return CreateProduct(product={'id': 2, 'name': name, 'description': description, 'price': price})

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    product_id = graphene.ID()

    def mutate(self, info, id):
        # Resolver function to delete a product by ID
        # This is where you would typically delete the product from your database
        # For demonstration purposes, let's return the ID of the deleted product
        return DeleteProduct(product_id=id)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)