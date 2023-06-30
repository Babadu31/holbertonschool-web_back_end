-- creates index IN TABLE names & first letter of name & score

CREATE INDEX idx_name_first_score
ON names (name(1), score);
