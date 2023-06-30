-- creates trigger to reset valid_email when email is changed

DELIMITER //

CREATE TRIGGER VALIDATE_EMAIL BEFORE UPDATE ON USERS
FOR EACH ROW BEGIN
	IF OLD.email != NEW.email THEN SET NEW.valid_email = 0;
	END IF;
END;

//

DELIMITER ;
