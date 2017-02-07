CREATE TABLE if not EXISTS `todo` (
  `id` INTEGER primary key autoincrement not null,
  `title` char(256) not null,
  `desc` text not null,
  `start` DATE not null,
  `end` DATE not null,
  `level` INTEGER,
  `status` char(256) not null
);