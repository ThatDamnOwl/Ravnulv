DROP FUNCTION IF EXISTS racktables_django.033_api_file_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.033_api_file_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_file);


    INSERT INTO 
        racktables_django.api_file (oldid, name, created, size, modified, accessed, thumbnail, content, comment, filetype)
        SELECT 
               id
              ,name
              ,ctime
              ,size
              ,mtime
              ,atime
              ,thumbnail
              ,contents
              ,ifnull(comment,'')
              ,type
        FROM 
             racktables.File
        WHERE 
            id NOT IN (SELECT oldid FROM racktables_django.api_file);
    SET inserted = (SELECT count(id) FROM racktables_django.api_file) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
