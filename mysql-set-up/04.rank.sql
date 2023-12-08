
-- SELECT card_value
-- FROM all_hands
-- WHERE hands = '1s 1h 1d 2s 3h'

-- SELECT ( 2598960 - COUNT(hands) )/2598960*100 as PR, COUNT(hands)
-- FROM all_hands
-- WHERE card_value > 71402000000


-- SELECT COUNT(card_value)
-- FROM all_hands


-- SELECT card_value
-- FROM all_hands
-- WHERE hands = '1s 1h 1d 2s 2h'

-- SELECT ( 2598960 - COUNT(hands) )/2598960*100 as PR, COUNT(hands)
-- FROM all_hands
-- WHERE 
-- card_value > ( 
--     SELECT card_value
--     FROM all_hands
--     WHERE hands = '2s 2h 2d 3h 4h' )
-- ;

-- CREATE TABLE rank_table AS 
-- SELECT *, RANK( ) OVER( ORDER BY card_value DESC) ranking
-- FROM all_hands 

SELECT ranking
FROM rank_table
WHERE hands = '1s Jh Qd Ks Kh'