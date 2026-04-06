import java.util.*;
import java.util.stream.Collectors;

public class task {
    public static void main(String[] args) {

        List<String> users = List.of(
                "alice:30",
                "bob:25",
                "charlie:35",
                "david:125"
        );
      //  System.out.println(users);

        // Используем stream api и преобразуем List в Map<String, Integer>
        Map<String, Integer> userTable = users.stream()
                .collect(Collectors.toMap(
                        x -> x.split(":")[0],                    // извлекаем имя
                        x -> Integer.parseInt(x.split(":")[1])  // извлекаем возраст и преобразуем в число
                ));
        //  System.out.println(userTable);


        Map.Entry<String, Integer> oldestPerson = userTable.entrySet().stream()
                .max(Map.Entry.comparingByValue())  // ищем пару с максимальным возрастом
                .orElse(null);  // если нет данных — null (но у нас есть)
        //System.out.println(oldestPerson);

        System.out.println(oldestPerson.getKey() + ":" + oldestPerson.getValue());

    }
}