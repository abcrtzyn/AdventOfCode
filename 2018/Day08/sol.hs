
import System.IO


data FileTree = Node [FileTree] [Int]


parseMeta:: Int -> [Int] -> [Int]


parseTree:: [Int] -> FileTree
parseTree [] = 




main = do
    withFile "Day08/test_input.txt" ReadMode (\f -> do
        contents <- hGetContents f
        return parseTree (map read (words contents))
        
        )
