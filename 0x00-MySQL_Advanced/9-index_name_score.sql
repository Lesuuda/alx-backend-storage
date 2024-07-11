-- creates an index of first later of
-- first name and on score
CREATE INDEX idx_name_first_score ON names(name(1), score);
