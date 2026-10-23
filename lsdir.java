import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.stream.Stream;


public class ListDirectory {

    public static void main(String[] args) {
        String dirPath;
        if (args.length > 0) {
            dirPath = args[0];
        } else {
            dirPath = "."; //Use current directory if no argument is specified
        }

        listDirectory(dirPath);
    }


    public static void listDirectory(String dirPath) {
        Path path = Paths.get(dirPath);

        try (Stream<Path> paths = Files.list(path)) {
            paths.forEach(filePath -> {
                try {
                    File file = filePath.toFile();
                    String fileName = file.getName();
                    String type = file.isDirectory() ? "Directory" : "File";
                    System.out.printf("- %s (%s)%n", fileName, type);
                } catch (Exception e) {
                    System.err.printf("Error processing file/directory: %s%n", e.getMessage());
                }
            });
        } catch (IOException e) {
            System.err.printf("Error reading directory '%s': %s%n", dirPath, e.getMessage());
        } catch (SecurityException e){
            System.err.printf("Insufficient permissions to access directory '%s'%n", dirPath);
        }

    }
}

