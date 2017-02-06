CREATE TABLE if not EXISTS `posts` (
  `id` INTEGER primary key autoincrement not null,
  `title` char(256) not null,
  `content` text not null,
  `pub_date` DATE not null,
  `author` text not null,
  `tags` char(256)
);

INSERT into `posts` (title, content, pub_date, author, tags) values ("post1", "hello from flask", "2017-02-01 12:03:21", "Bruce Lee", "test,first");
INSERT into `posts` (title, content, pub_date, author, tags) values ("post2", "hello again from flask", "2017-02-11 12:13:21", "Bruce Lee", "test");