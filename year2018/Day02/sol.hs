import System.IO
import Data.List (sort,group,foldl')
import Control.Monad (replicateM)

mapTuple :: (a -> b) -> (a, a) -> (b, b)
mapTuple f (x,y) = (f x, f y)

countTrues :: [Bool] -> Int
countTrues = foldl' (\x y -> x + if y then 1 else 0) 0

countTwoPred :: Eq a => (a -> Bool) -> (a -> Bool) -> [a] -> (Int,Int)
countTwoPred f1 f2 l = mapTuple countTrues (unzip (map (\e -> (f1 e, f2 e)) l))

part1 :: [String] -> Int
part1 ss = case countTwoPred (2 `elem`) (3 `elem`) (map (map length . group . sort) ss) of
    (x, y) -> x * y


-- I need a cross product
cartesianProduct :: [a] -> [b] -> [(a,b)]
cartesianProduct l1 l2 = [(x,y) | x <- l1, y <- l2]

stringDistance :: String -> String -> Int
stringDistance s1 s2 = countTrues $ zipWith (/=) s1 s2



-- part2 :: [String] -> S
part2 ss = let matches = filter ((1 ==) . uncurry stringDistance) (cartesianProduct ss ss) in
    -- the cartesian product outputs two matches per
    if length matches == 2 then
        filter (/= ' ') (uncurry (zipWith (\x y -> if x==y then x else ' ')) (head matches))
        --  (\x y -> if x == y then x else ' ') (head matches)
    else 
        "Multiple matches" ++ show matches
    



main :: IO ()
main = do
    withFile "Day02/input.txt" ReadMode (\file -> do
        contents <- fmap lines (hGetContents file)
        putStrLn $ "Part 1: " ++ show (part1 contents)
        putStrLn $ "Part 2: " ++ part2 contents
        )
