
from sqlalchemy import Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase
from sqlalchemy.orm import declarative_base

dsn = "sqlite:///hometask15.db"
engine = create_engine(dsn, echo=True)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

Base = declarative_base()



class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64))
    phone = Column(String(64))

    products = relationship("Product", back_populates="seller")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    cost = Column(Float)
    count = Column(Integer)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    seller = relationship(Seller, back_populates="products")
    orders = relationship("Order", back_populates="product")


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64),  unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"User: {self.username}"


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    count = Column(Integer)

    user = relationship(User, back_populates="orders")
    product = relationship(Product, back_populates="orders")

    def __str__(self):
        return f"Id: {self.id}, user_id:{self.user_id}, product_id: {self.product_id}, count:{self.count} "

def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def add_users(connection: Session):

    connection.add(
        User(username="igor", password="<PASSWORD>", email="igor@mail.com"))

    connection.add(
        User(username="Dima", password="<PASSWORD>", email="dima@gmail.com"))

    connection.add(
        User(username="user123", password="<PASSWORD>", email="user123@mail.com")
    )
    connection.add(
        User(username="user111", password="<PASSWORD>", email="user111@mail.com")
    )
    connection.add(
        User(username="user999", password="<PASSWORD>", email="user999@mail.com")
    )

    connection.commit()


def add_sellers(connection):
    connection.add(Seller(company="LVMH", phone="1254563222"))
    connection.add(Seller(company="samsung", phone="554785444"))
    connection.add(Seller(company="snickers", phone="54478"))
    connection.add(Seller(company="solidgear", phone="66698774"))
    connection.commit()


def add_products(connection, seller):
    connection.add(Product(name='tshirt', cost=54.5, count=2, seller_id=seller.id))
    connection.add(Product(name='pants', cost=99, count=21, seller_id=seller.id))
    connection.add(Product(name='shoes', cost=150.5, count=50, seller_id=seller.id))
    connection.add(Product(name='vest', cost=200, count=10, seller_id=seller.id))
    connection.commit()


def create_order(connection: Session, user: User, product, count):
    order = Order(user_id=user.id, product_id=product.id, count=count)
    connection.add(order)
    connection.commit()


drop_tables()
create_tables()

add_users(session)
add_sellers(session)
print("="*100)

query = select(User).where(User.username=='Dima')
user_dima = session.execute(query).scalars().one()
print(user_dima)
print("="*100)

query = select(User)
users = session.execute(query).scalars()
for user in users:
    print(f" usernme: {user.username}")
print("="*100)

query = select(Seller)
sellers = session.execute(query).scalars()
for seller in sellers:
    print(f"seller:-{seller.id} --- {seller.company}")
print("="*100)

seller = session.query(Seller).filter_by(company='solidgear').first()
add_products(session, seller)
print("="*100)

product_tshirt= session.query(Product).filter_by(name="tshirt").first()
create_order(session, user_dima, product_tshirt,6)
query = select(Order).filter(Order.id == 1)
order = session.execute(query).scalars().one()
print(order)
print("="*50)


def get_all_user_order(session,user_name):
    all_user_order = session.query(Order).filter(Order.id == 1).join(User).filter(User.username == user_name)
    for l in all_user_order:
        print(l)
        print("="*100)


get_all_user_order(session,"Dima")

def get_seller_product(session, name_company):
    all_product = session.query(Product).join(Seller).filter(Seller.company == name_company)
    for product in all_product:
        print(f"prdduct name: {product.name} cost: {product.cost}, seller: {seller.company}")
    print("="*100)

get_seller_product(session,'solidgear')

