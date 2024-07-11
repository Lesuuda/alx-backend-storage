-- creates a trigger that decreaes the quantity
-- of an itm after adding a new order
DROP TRIGGER IF EXISTS reduce_quantity;
DELIMITER $$
CREATE TRIGGER reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN 
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_name;
END $$
DELIMITER ;
