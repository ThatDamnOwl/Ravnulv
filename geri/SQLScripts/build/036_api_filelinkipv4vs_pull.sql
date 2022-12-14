DROP FUNCTION IF EXISTS racktables_django.036_api_filelinkipv4vs_pull;

DELIMITER $$
CREATE FUNCTION racktables_django.036_api_filelinkipv4vs_pull (ignored BIGINT)
RETURNS INT
NOT DETERMINISTIC
BEGIN
    DECLARE inserted INT;
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4vs);
    INSERT INTO 
        racktables_django.api_filelinkipv4vs (oldid,file_id,parent_id) 
        SELECT 
               FL.id
              ,apifile.id
              ,apiobj.id
        FROM 
             racktables.FileLink FL
             LEFT JOIN racktables_django.api_file as apifile on file_id = apifile.oldid
             LEFT JOIN racktables_django.api_ipv4vs as apiobj on entity_id = apiobj.oldid
        WHERE 
            FL.id NOT IN (SELECT oldid FROM racktables_django.api_filelinkipv4vs) AND
            entity_type = 'ipv4vs';
    SET inserted = (SELECT count(id) FROM racktables_django.api_filelinkipv4vs) - inserted;
    RETURN inserted;
END;
$$ 
DELIMITER ;
