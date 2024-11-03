//! not functional
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

class P3_2 {

    public static void main(String[] args) {
        
        try (Stream<String> linesStream = Files.lines(Paths.get("input.txt"))) {
            linesStream.map(String::toCharArray)
        }
    }
}