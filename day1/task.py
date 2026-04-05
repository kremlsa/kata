# Дано
# JSON:
# [
#   {"cve": "CVE-1", "severity": "low"},
#   {"cve": "CVE-2", "severity": "critical"},
#   {"cve": "CVE-3", "severity": "high"},
#   {"cve": "CVE-4", "severity": "CRITICAL"},
#   {"cve": "CVE-5", "severity": "critical"},
#   {"cve": "CVE-6", "severity": "Critical"},
#   {"cve": "CVE-7", "severity": null},
#   {"cve": "CVE-8", "severity": "low"},
#   {"cve": "CVE-9", "severity": "critical\n"},
#   {"cve": "CVE-10", "severity": "critical "}
# ]
#
#
# Сделать
#
# Вывести имена только critical уязвимостей
# Ожидаемый результат
# CVE-2
# CVE-4
# ...
#
data = [
  {"cve": "CVE-1", "severity": "low"},
  {"cve": "CVE-2", "severity": "critical"},
  {"cve": "CVE-3", "severity": "high"},
  {"cve": "CVE-4", "severity": "CRITICAL"},
  {"cve": "CVE-5", "severity": "critical"},
  {"cve": "CVE-6", "severity": "Critical"},
  {"cve": "CVE-7", "severity": None},
  {"cve": "CVE-8", "severity": "low"},
  {"cve": "CVE-9", "severity": "critical\n"},
  {"cve": "CVE-10", "severity": "critical "}
]

def parse_cve(data):
    result = []
    for item in data:
        severity = item['severity']
        if severity is not None:
            severity = severity.replace(' ', '').replace('\n', '') #вот тут санитизация
        else:
            continue
        if severity.lower() == 'critical': #а вот тут валидация
            result.append(item["cve"])
    return result


for cve in parse_cve(data):
    print(cve)
