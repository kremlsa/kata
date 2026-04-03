import java.util.ArrayList;
import java.util.List;

public class SeqSelector {
    public static void main(String[] args) {
        List<String> logs = List.of(
                "INFO User logged in",
                "ERROR Database connection failed",
                "INFO Request processed",
                "ERROR NullPointerException",
                "WARN Disk almost full"
        );

        int count = logs.size();
        int i = 0;

        List<String> resultLogs = new ArrayList<>();

        //Не используем цикл for
        while (i < count) {
            if (logs.get(i).startsWith("ERROR")) {
                String deleteFirstWord = logs.get(i).substring(logs.get(i).indexOf(' ') + 1);
                resultLogs.add(deleteFirstWord);
            }
            i++;
        }

        resultLogs.forEach(System.out::println);
    }
}
