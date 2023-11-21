from sqlalchemy import Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Строка подключения (DSN)

# Диалект - `sqlite`
# Обращение - `://`
# Путь - `/test.db` (В текущей папке)
dsn = "sqlite:///test.db"

# Точка входа в БД.
# `echo=True` - будут выводиться все действия с базой.
engine = create_engine(dsn, echo=True)

# Создаем новый класс для сессий, которые использует `engine`
# `autoflush=False` - убираем автоматическое подтверждение действий.
session = sessionmaker(bind=engine, autoflush=False)


# Создаем декларативную основу для будущих классов
class Base(DeclarativeBase):
    pass


# Создаем декларативное описание нашей таблицы
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable=False это NOT NULL
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    def __str__(self):
        return f"User: {self.username}"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    price = Column(Float)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))


def create_tables():
    # Создаем таблицы, которые унаследованы от `Base`
    Base.metadata.create_all(engine)


def drop_tables():
    # Удаляем таблицы, которые унаследованы от `Base`
    Base.metadata.drop_all(engine)


def add_users(connection):
    # Создали объект python. В базе его нет!

    user = User(username="igor", password="<PASSWORD>", email="igor@mail.com")

    # Добавим в таблицу запись через подключение
    connection.add(user)
    connection.add(
        User(username="user123", password="<PASSWORD>", email="user123@mail.com")
    )
    connection.add(
        User(username="user111", password="<PASSWORD>", email="user111@mail.com")
    )
    connection.add(
        User(username="user999", password="<PASSWORD>", email="user999@mail.com")
    )

    # Подтверждаем добавление!
    connection.commit()


def add_products(connection):
    connection.add(Product(name="tv", price=111))
    connection.add(Product(name="ps5", price=222))
    connection.add(Product(name="pc", price=333))
    connection.add(Product(name="monitor", price=444))
    connection.commit()


def create_order(connection, user: User, product: Product):
    order = Order(user_id=user.id, product_id=product.id)
    connection.add(order)
    connection.commit()


def show_user_orders(connection, username: str):
    pass


drop_tables()
create_tables()

with session() as conn:
    add_users(conn)  # Добавили пользователей

    add_products(conn)  # Добавили товары

    # Отобразить всех пользователей!

    # Создаем запрос
    query = select(User)  # select * from users;

    users = conn.execute(query).scalars()  # Выполняем запрос!
    # Через метод `scalars()` получаем перечень объектов `User`
    # users это тип `ScalarResult[User]` - перечень (итератор).

    for user in users:
        print(user.username, user.email)

    query = select(User).where(User.username == "igor")

    # Так как пользователь только 1 с таким username, то можно сделать `one()`
    user = conn.execute(query).scalars().one()

    query = select(Product).where(Product.name == "tv")
    product = conn.execute(query).scalars().one()

    create_order(conn, user, product)

    show_user_orders(conn, "igor")
