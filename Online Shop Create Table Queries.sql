create table customer(
username varchar(20) not null unique,
c_f_name varchar(20) not null,
c_l_name varchar(20) not null,
gender varchar(6),
email varchar(255) not null,
address varchar(255),
pass_word varchar(20) not null,
phone varchar(11),
primary key (username)
);


create table category(
category_id int not null,
category_name varchar(50),
primary key (category_id)
);

create table basket(
    basket_id int not null,
    totalprice int,
    product_id int,
    price int,
    customer_id varchar(20),
    foreign key (customer_id) references customer(username),
    primary key (basket_id),
);

create table product(
product_id int,
product_name varchar(50),
price bigint,
product_number int,
category_id int,
basket_id int,
foreign key (category_id) references category(category_id),
foreign key (basket_id) references basket(basket_id), 
primary key(product_id)
);

create table t_comment(
comment_id int not null,
customer_id varchar(20),
product_id int,
comment_text varchar(255),
foreign key(customer_id) references customer(username),
foreign key(product_id) references product(product_id),
primary key(comment_id)
);

create table stars(
comment_id int not null,
number_of_stars int ,
customer_id varchar(20),
product_id int,
foreign key (customer_id) references customer(username),
foreign key (product_id) references product(product_id),
primary key (comment_id)
);


create table pay(
    pay_id int not null,
    basket_id int,
    totalpay int,
    date_p varchar(20),
    foreign key (basket_id) references basket(basket_id),
    primary key (pay_id),
);

create table oreder(
    order_id int not null,
    basket_id int,
    customer_id varchar(20),
    date_order varchar(20),
    totalpay int,
    region_id int,
    foreign key (order_id) references pay(pay_id),
    foreign key (customer_id) references customer(username),
    primary key(order_id),
);

create table post(
    post_id int not null,
    date_p varchar(20),
    sent_p varchar(20),
    totalpay int,
    region_id int,
    address varchar(255),
    phone varchar(11),
    customer_id varchar(20),
    foreign key (post_id) references oreder(order_id),
    foreign key (customer_id) references customer(username),
    primary key(post_id),

);

CREATE TABLE seller
(
    seller_Id INT NOT NULL PRIMARY KEY, 
    name [NVARCHAR](50) NOT NULL
);

CREATE TABLE product_sellers
(
    p_number int NOT NULL,
    price int NOT NULL,
    p_id int not NULL,
	seller_id int not null,
    foreign key (p_id) references product(product_id),
	foreign key (seller_id) references seller(seller_id),

);
CREATE TABLE attribute
(
    attribute_id  int NOT NULL primary key,
    attribute VARCHAR(25) NOT NULL,
    category_id int NOT NULL,
    foreign key (category_id) references category(category_id)
);
CREATE TABLE value
(
    value_id int NOT NULL PRIMARY key,
    attribute_id int NOT NULL,
    product_id int NOT NULL,
    category_id int NOT NULL,
    VALUE VARCHAR(50) NULL,
    foreign key (category_id) references category(category_id),
    foreign key (product_id) references product(product_id),
    foreign key (attribute_id) references attribute(attribute_id),

);


