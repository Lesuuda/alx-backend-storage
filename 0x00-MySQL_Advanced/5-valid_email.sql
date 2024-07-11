-- creates a trigger that resets the attribute valid_email
DROP TRIGGER IF EXISTS valid_email;
DELIMITER $$
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN 
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    Else
         SET NEW.valid_email = NEW.valid_email;
        END IF;
END $$
DELIMITER ;
