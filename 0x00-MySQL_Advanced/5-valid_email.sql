-- Create a trigger to reset the valid_email attribute when the email is changed
DELIMITER //

CREATE TRIGGER before_update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;

//

DELIMITER ;
