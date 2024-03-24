-- a SQL script that creates a view need_meeting
-- Task 11: No table for a meeting

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80 AND last_meeting IS NULL)
    OR (score < 80 AND last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
