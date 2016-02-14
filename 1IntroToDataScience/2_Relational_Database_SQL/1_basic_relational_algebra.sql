/*
sqlite3 reuters.db < sql_filename
*/

/* a. Select */
select count (*) from 
(SELECT * FROM frequency WHERE docid = '10398_txt_earn');

/*b. Select and Project*/
select count (*) from 
(SELECT term FROM frequency
 WHERE docid = '10398_txt_earn' and count = 1);

/*c. Union*/
select count (*) from 
(SELECT term FROM frequency
 WHERE docid = '10398_txt_earn' and count = 1
 UNION 
 SELECT term FROM frequency
 WHERE docid = '925_txt_trade' and count = 1
 );

/*d. Count */
select count (*) from 
(
	SELECT docid FROM frequency
 	WHERE term = 'law'
 	UNION
 	SELECT docid FROM frequency
 	WHERE term = 'legal'
 );

/*e. Big Documents */
select count (*) from 
(
	SELECT docid FROM frequency
 	GROUP BY docid
	HAVING count(term) > 300
);

/*f. Find intersection*/
select count (*) from 
(SELECT a.docid
 FROM frequency AS a
 INNER JOIN frequency AS b
 ON a.term = 'transactions' AND b.term = 'world' 
 AND a.docid = b.docid
 );

/*g. test*/
select count (*) from 
(SELECT DISTINCT a.docid
 FROM frequency AS a
 WHERE a.term = 'world'
 );

/*
h. SIMILARITY
The query will return four sets
<a,a> <a, b> and <b, a>, <b,b>, 
if do not add the a.docid < b.docid
*/


DROP VIEW a;
DROP VIEW b;

CREATE VIEW a AS
SELECT * FROM frequency where frequency.docid = '10080_txt_crude' or frequency.docid = '17035_txt_earn' ;

CREATE VIEW b AS
SELECT * FROM frequency where frequency.docid = '10080_txt_crude' or frequency.docid = '17035_txt_earn' ;

SELECT a.docid, b.docid, SUM(a.count * b.count)
FROM a, b
WHERE a.term = b.term and a.docid < b.docid
GROUP BY a.docid, b.docid;



/* i. keyword search*/

DROP VIEW c;
DROP VIEW a;
DROP VIEW b;

CREATE VIEW c AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

CREATE VIEW a AS
SELECT * FROM c;

CREATE VIEW b AS
SELECT * FROM c;

SELECT * 
FROM (
	SELECT a.docid, b.docid, SUM(a.count * b.count) AS count
	FROM a, b
	WHERE a.term = b.term
	GROUP BY a.docid, b.docid
)
WHERE docid = 'q'
ORDER BY count DESC;
