-- CREATE VIEW add_category AS
-- SELECT *, FLOOR(card_value / 10000000000) AS category
-- FROM all_hands
-- ;

SELECT category, count(hands) 
FROM add_category
GROUP BY category
ORDER BY category DESC;
