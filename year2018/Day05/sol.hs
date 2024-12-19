import System.IO
import Data.Char
import Data.Traversable (for)


swapCase :: Char -> Char
swapCase c = if isLower c then toUpper c else toLower c

canReact :: Char -> Char -> Bool
canReact a b = a == swapCase b


react :: String -> String
react "" = ""
react (x:xs) = case react xs of
    "" -> [x]
    x':xs' -> if canReact x x' then xs' else x:x':xs'


part1 :: String -> Int
part1 = length . react


-- It appears that if I react, then remove, and react again, the result should be the same
-- And since after the first reaction the string is 9000 chars, it should be faster

f :: String -> Char -> String
f s letter = filter (\c -> c /= letter && c /= toLower letter) s

part2Helper :: String -> [String]
part2Helper s = map (f s) "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

part2 :: String -> Int
part2 s = minimum (map (length . react) (part2Helper s))

-- for each letter in the alphabet
-- filter it out of the string



main :: IO ()
main = do
    withFile "Day05/input.txt" ReadMode (\file -> do
        contents <- hGetContents file
        -- init removes the final character which is a newline, would rather make a strip function
        putStrLn $ "Part 1: " ++ show (part1 (init contents))
        putStrLn $ "Part 2: " ++ show (part2 (init contents))
        )
