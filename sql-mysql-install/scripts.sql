-- --------------------------------------------------------

--
-- Структура таблицы "Пользователи"
--
-- `id` - ID пользователя
-- `annotation` - аннотация на аккаунт
-- `name` - имя (ник)
-- `country` - страна
-- `hobby_one` - хобби первое
-- `hobby_two` - хобби второе
-- `hobby_three` - хобби третье
-- `hobby_four` - хобби четвёртое
-- `hobby_five` - хобби пятое
-- `favorite_os` - любимая ОС
-- `language_one` - ЯП первое
-- `language_two` - ЯП второе
-- `language_three` - ЯП третье
-- `language_four` - ЯП четвёртое
-- `language_five` - ЯП пятое
--

CREATE TABLE `users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`annotation` VARCHAR(255) NOT NULL,
	`name` VARCHAR(20) NOT NULL,
	`country` VARCHAR(30) NOT NULL,
	`hobby_one` VARCHAR(30) NOT NULL,
	`hobby_two` VARCHAR(30) NULL,
	`hobby_three` VARCHAR(30) NULL,
	`hobby_four` VARCHAR(30) NULL,
	`hobby_five` VARCHAR(30) NULL,
	`favorite_os` VARCHAR(30) NOT NULL,
	`language_one` VARCHAR(30) NOT NULL,
	`language_two` VARCHAR(30) NULL,
	`language_three` VARCHAR(30)  NULL,
	`language_four` VARCHAR(30) NULL,
	`language_five` VARCHAR(30) NULL,
	PRIMARY KEY (`id`))
	ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;