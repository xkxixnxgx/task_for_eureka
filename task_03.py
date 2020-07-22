# Задача:
# На вход подаётся параметр query.
# При этом query может быть: Иванов Сергей Петрович, Сергей Иванов,
# Сергей Петрович Иванов, Сергей и т.д
# Написать запрос, возвращающий записи, в ФИО которых входят слова из query
# ! Если query='иван иван' возвращаем 3 запись, а первую не возвращаем

# Исходные данные:
# -- DDL and sample data population, start
# DECLARE @tbl TABLE (
#   id int NOT NULL,
#   last_name Nvarchar(100) NOT NULL,
#   first_name Nvarchar(100) NOT NULL,
#   middle_name Nvarchar(100) NOT NULL
# );
# INSERT INTO @tbl (id, last_name, first_name, middle_name)
# VALUES
#   ('1', N'Иванов', N'Андрей', N'Петрович'),
#   ('2', N'Петров', N'Иван', N'Андреевич'),
#   ('3', N'Иванов', N'Виталий', N'Иванов'),
#   ('4', N'Сергеев', N'Петр', N'Витальевич'),
#   ('5', N'Андреев', N'Сергей', N'Сидорович');
# -- DDL and sample data population, end


# Решение:

DECLARE @Separator NCHAR(1) = SPACE(1)
	, @parameterXML NVARCHAR(1024)
	, @parameter NVARCHAR(100) = N'Иванов Иванов';

SET @parameterXML = N'<source><row>'
	+ REPLACE(@parameter, @Separator, N'</row><row>')
	+ N'</row></source>';

SELECT ID, last_Name, first_name, middle_name
   , CAST('<root>' + @parameterXML
		+ '<target><row>'
		+ last_name + '</row><row>'
		+ first_name + '</row><row>'
		+ middle_name + '</row>'
		+ '</target></root>' AS XML)
    .value('every $r in /root/source/row/text()
            satisfies ($r = (/root/target/row/text())
            and count(/root/source/row[./text()[1] eq $r]) = count(/root/target/row[./text()[1] eq $r])
         )', 'VARCHAR(5)') AS result
FROM @tbl;