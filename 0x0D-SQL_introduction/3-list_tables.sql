-- Lists tables on a database passed as command line argument


DELIMITER //
CREATE PROCEDURE ListTablesInDatabase(IN dbName VARCHAR(255))
BEGIN
    SET @query = CONCAT('USE', dbName);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SHOW TABLES;
END //
DELIMITER ;