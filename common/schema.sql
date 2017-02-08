CREATE TABLE if not EXISTS `posts` (
  `id` INTEGER primary key autoincrement not null,
  `title` char(256) not null,
  `content` text not null,
  `pub_date` DATE not null,
  `author` text not null,
  `tags` char(256)
);

CREATE TABLE if not EXISTS `users` (
  `id` INTEGER PRIMARY KEY autoincrement not null,
  `username` char(256) not null,
  `password` char(256) not null,
  `activated` bool not null default true,
  `permission_level` INTEGER not null default 10
);

INSERT into `users` (username, password) VALUES ('bruce', 'e8315caa4eb8c2a2625d4e97dbba100a')