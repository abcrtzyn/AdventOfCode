import System.IO
import Text.Read (readMaybe)
import Control.Monad.State.Lazy
import Data.Set (Set, member, insert, empty)

parseInput :: String -> Maybe [Int]
parseInput s = mapM readMaybe (lines (filter (/= '+') s))


part2 :: Int -> [Int] -> State (Set Int) Int
part2 _ [] = return (-1)
part2 acc (x:xs) = do
    -- check if the acc is in the set
    set <- get
    (if acc `member` set then return acc else (do
        -- add the acc to the set
        modify (insert acc)
        -- do the next
        part2 (x+acc) xs))



main :: IO ()
main = do
    withFile "Day01/input.txt" ReadMode (\file -> do
        contents <- hGetContents file

        case parseInput contents of
            Nothing -> putStrLn "Could not parse the input"
            Just l -> do
                putStrLn $ "Part 1: " ++ show (sum l)
                putStrLn $ "Part 2: " ++ show (evalState (part2 0 (cycle l)) empty)

        )
