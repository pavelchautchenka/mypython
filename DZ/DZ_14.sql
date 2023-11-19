

create database if not exists lesson;
use lesson;

CREATE TABLE sellers (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    company VARCHAR(64) NOT NULL,
    phone VARCHAR(64) NOT NULL
);

CREATE TABLE product (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name_product VARCHAR(64) NOT NULL,
    cost INT NOT NULL,
    total INT NULL,
    seller_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (seller_id)
        REFERENCES sellers (id)
);

create table users (
id int unsigned primary key auto_increment,
username varchar (32) not null,
passwd varchar (128) not null,
email varchar (64) default 'email is not defined' not null

constraint email_check check (email regexp '^[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+'),
constraint passwd_check check (length(passwd) >= 10)
);

CREATE TABLE orders (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id int unsigned not null,
    product_id INT unsigned not null,
    total INT,
    FOREIGN KEY (user_id)
        REFERENCES users (id),
    FOREIGN KEY (product_id)
        REFERENCES product (id)
);

insert into sellers ( company, phone) value( "LVMH", "5478565478");
insert into product ( name_product, cost, total,seller_id) value ("vest", "250", 2,1);
insert into users (username, passwd,email) value ("log" , "154545sqd5445dq", "fsfdsfs@dsqdsdq.com");
insert into orders (total, user_id, product_id) value ( 9, 1, 1) ;

select * from orders

