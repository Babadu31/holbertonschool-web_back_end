-- resets valid email table when email table has been changed

CREATE TRIGGER email_validator BEFORE UPDATE on users
    BEGIN
        IF NEW.email != OLDemail THEN
            SET NEW.valid_email = 0;
        END IF;
    END;
