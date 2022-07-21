#from . import DB, create_app


# class Payments(DB.Model):
#     id = DB.Column('payment_id',DB.Integer, primary_key = True)
#     email = DB.Column('email',DB.String(length=100),nullable=False, unique=True)
#     name = DB.Column('name',DB.String(length=50), nullable=False, unique=True)
#     message = DB.Column('message',DB.String(length=400), nullable=True)
#     payment_value = DB.Column('payment_value',DB.Integer(), nullable= False)
#     paytime = DB.Column('paytime',DB.String(length=20), nullable=False)

#     def __repr__(self) -> str:
#         return super().__repr__()