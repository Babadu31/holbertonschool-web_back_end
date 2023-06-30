-- creates a trigger to decrease the quantity of items in a store

CREATE TRIGGER buy AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
        SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
