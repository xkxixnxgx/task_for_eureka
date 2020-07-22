# Задание:

# SELECT * FROM docs WHERE p1='3' and p2='3' and p3='2' and p4='1' and p5='9'
# Написать запрос, в который вместо %p1..%p5 можно подставить значения параметров или null
# если параметр null, то у возвращенных записей этот параметр может быть любым
# SELECT * FROM docs WHERE p1=%p1 and p2=%p2 and p3=%p3 and p4=%p4 and p5=%p5


# Исходные данные:

# CREATE TABLE IF NOT EXISTS `docs` (
#   `id` int(6) unsigned NOT NULL,
#   `p1` varchar(10) NOT NULL,
#   `p2` varchar(10) NOT NULL,
#   `p3` varchar(10) NOT NULL,
#   `p4` varchar(10) NOT NULL,
#   `p5` varchar(10) NOT NULL,
#   PRIMARY KEY (`id`)
# ) DEFAULT CHARSET=utf8;

# INSERT INTO `docs` (`id`, `p1`, `p2`,`p3`,`p4`,`p5`) VALUES
#   ('1', '2', '3', '5', '1', '9'),
#   ('2', '1', '2', '9', '6', '4'),
#   ('3', '3', '3', '2','1', '9'),
#   ('4', '2', '6', '1', '7', '8'),
#   ('5', '3', '3', '1', '2', '7'),
#   ('6', '3', '2', '1', '8', '3'),
#   ('7', '1', '4', '2', '3', '2'),
#   ('8', '5', '9', '7', '4', '1');


# Решение:

# SELECT * FROM docs WHERE p1=coalesce(%p1,p1) and p2=coalesce(%p2,p2) and p3=coalesce(%p3,p3) and p4=coalesce(%p4,p4) and p5=coalesce(%p5,p5);

# Примечание:
# Несмотря на то, что данное решение работает, надо быть очень внимательным со значением null, а писать такие запросы - не лучшая практика.
# При составлении подобных динамических запросов следует более явно и подробно прописывать логику и условия.

