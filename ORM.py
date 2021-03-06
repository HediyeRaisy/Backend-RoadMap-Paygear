import os
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, session,sessionmaker, Session
from sqlalchemy.sql.expression import select, text, true
from sqlalchemy.sql.sqltypes import BigInteger


basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///'+ os.path.join(basedir, 'shop.sqlite'), echo=True)
Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

class Customer(Base):

    __tablename__ = 'customer'   
    username  = Column(String, primary_key=true)
    c_f_name  = Column(String)
    c_l_name  = Column(String)
    gender  = Column(String)
    email  = Column(String)
    address  = Column(String)
    pass_word  = Column(String)
    phone  = Column(String)
    customer_comment = relationship("Comment", back_populates="comment_customer")
    customer_star= relationship("Star", back_populates="star_customer")



class Category(Base):
    __tablename__ = 'category'  
    category_id  = Column(Integer, primary_key=true)
    category_name  = Column(String)
    category_product = relationship("Product", back_populates="product_category")



class Basket(Base):
    __tablename__ = 'basket'
    basket_id = Column(Integer,primary_key=True)
    totalprice = Column(Integer)
    product_id = Column(Integer)
    price = Column(Integer)
    customer_id = Column(String)
    basket_product = relationship("Product", back_populates="product_basket")




class Product(Base):

    __tablename__ = 'product'   
    product_id  = Column(Integer, primary_key=true)
    product_name  = Column(String)
    price  = Column(BigInteger)
    product_number  = Column(Integer)
    basket_id = Column(Integer,ForeignKey(Basket.basket_id))
    category_id = Column(Integer,ForeignKey(Category.category_id))
    product_basket = relationship("Product", back_populates="basket_product")
    product_category = relationship("Category", back_populates="category_product")
    product_comment = relationship("Comment", back_populates="comment_product")
    product_star = relationship("Star", back_populates="star_product")




class Comment(Base):
    __tablename__ = 'comment'  
    comment_id = Column(Integer, primary_key=true)
    comment_text = Column(String)
    customer_id = Column(String,ForeignKey(Customer.username))
    product_id = Column(Integer,ForeignKey(Product.product_id))
    comment_product = relationship("Product", back_populates="product_comment")
    comment_customer = relationship("Customer", back_populates="customer_comment")




class Star(Base):
    __tablename__ = 'star'  
    comment_id   = Column(Integer, primary_key=true)
    star_num  = Column(Integer)
    customer_id = Column(String,ForeignKey(Customer.username))
    product_id = Column(Integer,ForeignKey(Product.product_id))
    star_product = relationship("Product", back_populates="product_star")
    star_customer= relationship("Customer", back_populates="customer_star")





class Pay(Base):

    __tablename__ = 'pay'
    
 
    pay_id = Column(Integer,primary_key=True)
    basket_id = Column(Integer,ForeignKey(Basket.basket_id))
    basket = relationship("Basket", backref='pay') #one to many relationship
    totalpay = Column(Integer)
    data_p = Column(String)

class Order(Base):
    __tablename__ = 'order'

 
    order_id = Column(Integer,primary_key=True)
    pay_id = Column(Integer,ForeignKey(Pay.pay_id))
    pay = relationship(Pay, uselist=False)
    basket_id = Column(Integer)
    customer_id = Column(String)
    date_order = Column(String)
    totalpay = Column(Integer)
    region_id = Column(Integer)

class Post(Base):

    __tablename__ = 'post'

   
    post_id = Column(Integer,primary_key=True)
    order_id = Column(Integer,ForeignKey(Order.order_id)) #one to one relationship
    order = relationship(Order, uselist=False)
    date_p = Column(String)
    sent_p = Column(String)
    totalpay = Column(Integer)
    region_id = Column(Integer)
    customer_id = Column(String)
    address = Column(String)
    phone = Column (String)





# session = Session()
# c1=Basket(
#     basket_id = 1,
#     totalprice = 123,
#     product_id = 1,
#     price = 123,
#     customer_id = 9810,
# )
# session.add(c1)
# print(c1.basket_id)
# session.commit()
# print(c1.basket_id)

class Seller(Base):
    
    __tablename__ = 'seller'

   
    seller_id = Column(Integer,primary_key=True)
    name = Column(String)
 

class Product_sellers(Base):
    
    __tablename__ = 'product_sellers'

   
    p_number = Column(Integer,primary_key=True)
    p_id = Column(Integer,ForeignKey(Product.product_id)) #one to one relationship
    price = Column(Integer)
    seller_id = Column(Integer,ForeignKey(Seller.seller_id))


class Attribute(Base):
    
    __tablename__ = 'attribute'

   
    attribute_id = Column(Integer,primary_key=True)
    category_id = Column(Integer,ForeignKey(Category.category_id))
    attribute = Column(String)

class Value(Base):
    
    __tablename__ = 'value'

   
    value_id = Column(Integer,primary_key=True)
    attribute_id =relationship("attribute", backref='attribute_id')
    product_id = Column(Integer,ForeignKey(Product.product_id))
    category_id = Column(Integer,ForeignKey(Category.category_id))
    VALUE = Column(String)

Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
# session = Session()
# c23=Basket(
#     value_id = 465,
#     VALUE = 74,
# )
# session.add(c23)
# print(c23.value_id)
# session.commit()

def create_customer_and_basket(username, f_name, l_name, gender, email, address, password, phone_num, basket_id):
    customer = Customer()
    customer.username = username
    customer.c_f_name = f_name
    customer.c_l_name = l_name
    customer.gender = gender
    customer.email = email,
    customer.address = address
    customer.pass_word = password
    customer.phone = phone_num


    basket = Basket()
    basket.basket_id = basket_id
    basket.totalprice = 0
    basket.product_id = 0
    basket.price = 0
    basket.customer_id = username

    Session.add(customer)
    Session.add(basket)

    Session.commit()
    


def create_comment_and_star(comment_id, comment_text, star_num, customer_id, product_id):

    comment = Comment()
    comment.comment_id = comment_id
    comment.customer_id = customer_id
    comment.comment_text = comment_text
    comment.product_id = product_id


    star = Star()
    star.comment_id = comment_id
    star.customer_id = customer_id
    star.star_num = star_num
    star.product_id = product_id

    Session.add(comment)
    Session.add(star)

    Session.commit()


def select_customer(customer_username):
    
    customer = Session.query(Customer) \
        .filter(Customer.username == customer_username) \
        .first()
 
    return customer

def select_basket(basket_id):
    
    basket = Session.query(Basket) \
        .filter(Basket.basket_id == basket_id) \
        .first()
 
    return basket


def select_text_comment(comment_id):
    
    text_comment = Session.query(Comment) \
        .filter(Comment.comment_id == comment_id) \
        .first()
 
    return text_comment


def select_star_comment(comment_id):
    
    star_comment = Session.query(Star) \
        .filter(Star.comment_id == comment_id) \
        .first()
 
    return star_comment

def create_pay(basket_id,date_p,pay_id):
    pay = Pay()
    pay.pay_id = pay_id
    pay.data_p = date_p
    basket = session.query(Basket).get(basket_id)
    pay.totalpay = basket.totalprice
    pay.basket_id = basket_id

def create_order(order_id,pay_id,date,region_id,customer_id):
    order = Order()
    order.order_id = order_id
    order.pay_id = pay_id
    pay = session.query(Pay).get(pay_id)
    order.basket_id = pay.basket_id
    order.customer_id = customer_id
    order.date_order = date
    order.region_id = region_id
    order.totalpay= pay.totalpay

def create_post(post_id,order_id,date,sent,customer_id):

    post = Post()
    post.post_id = post_id
    post.order_id = order_id
    post.date_p = date
    post.sent_p = sent
    post.customer_id = customer_id
    customer = session.query(Customer).get(customer_id)
    post.phone = customer.phone
    post.address = customer.address
    order = session.query(Order).get(order_id)
    post.region_id = order.region_id
    post.totalpay = order.totalpay

def create_seller(seller_id,name):
    seller = Seller()
    seller.name = name
    seller.seller_id = seller_id

def create_product_seller(p_id,price,p_number,seller_id):
    ps = Product_sellers()
    ps.p_id = p_id
    ps.p_number = p_number
    ps.price = price
    ps.seller_id = seller_id






