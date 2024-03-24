--  creates a function SafeDiv that divides the first by the second number
-- 10. Safe divide

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END//

DELIMITER ;
