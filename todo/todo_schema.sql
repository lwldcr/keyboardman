CREATE TABLE if not EXISTS `todo` (
  `id` INTEGER primary key autoincrement not null,
  `category_id` INTEGER not null default 0,
  `title` char(256) not null,
  `desc` text not null,
  `start` DATE not null,
  `end` DATE not null,
  `level` INTEGER,
  `status` char(256) not null
);

CREATE TABLE if NOT EXISTS `category` (
  `id` INTEGER PRIMARY KEY autoincrement not null,
  `name` char(32) not null,
  `extra` char(64)
);