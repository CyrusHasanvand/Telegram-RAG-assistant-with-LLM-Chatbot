create database ChatBotDB2;
use ChatBotDB2;

create table logs (
	id INT auto_increment primary KEY,
    user_id bigint,
    username varchar(100),
    message text,
    reply text,
    create_at Timestamp default current_timestamp
);


