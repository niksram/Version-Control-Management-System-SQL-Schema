--all contributors in android repository
SELECT file_name,contributor from files WHERE repo_name='android';
--all employees working on the london server
SELECT fname,lname FROM employee NATURAL JOIN server WHERE location='London';
--All contributors to the server managed by Ramesh Ranganathan
SELECT contributor from commits where repo_name in (SELECT repo_name FROM employee NATURAL JOIN repository where fname='Ramesh' and lname='Ranganathan');
--average age of python coders
SELECT AVG(age) FROM coder where username in (SELECT contributor FROM COMMITS NATURAL JOIN extension WHERE FILE_TYPE='python' AND type='INSERT');
--distribution of file_types in a repository
SELECT file_type,count(file_type) FROM repository NATURAL JOIN (SELECT * FROM extension,files where files.file_extension=extension.extension) as F WHERE repo_name='android' GROUP BY file_type;