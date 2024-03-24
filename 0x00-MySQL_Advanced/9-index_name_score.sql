-- creates an index idx_name_first_score on the table names
-- Optimize search and score

CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
