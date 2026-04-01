// Дано:
// список строк (имитация логов):
//
// List<String> logs = List.of(
//     "INFO User logged in",
//     "ERROR Database connection failed",
//     "INFO Request processed",
//     "ERROR NullPointerException",
//     "WARN Disk almost full"
// );
//
//
// Сделать:
// Отфильтровать только строки с "ERROR"
// Преобразовать их в новый список, содержащий только текст ошибки (без слова ERROR)
// Вывести результат
//
// Ожидаемый результат:
//
// Database connection failed
// NullPointerException
//
// Ограничения:
// Без циклов for (при возможности)
