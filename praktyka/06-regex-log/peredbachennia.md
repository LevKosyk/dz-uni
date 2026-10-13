`re.search(r'"(.*)"', ryadok).group(1)`

**Передбачення:** 16.4.101 - - [17/Mar/2026:08:01:26 +0200] "GET /catalog.html HTTP/1.1" 200 30522 "https://example.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5) Safari/605.1.15" - Не вгадав - 'GET /catalog.html HTTP/1.1" 200 30522 "https://example.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5) Safari/605.1.15'

`re.search(r'"(.*?)"', ryadok).group(1)`

**Передбачення:**  16.4.101 - - [17/Mar/2026:08:01:26 +0200] "GET /catalog.html HTTP/1.1" 200 30522 "https://example.com/" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5) Safari/605.1.15Не знаю - Не вгадав - 'GET /catalog.html HTTP/1.1'

`re.search(r'(\d{3}) (\d+)', ryadok).groups()`

**Передбачення:** '200', '30522' - Вгадав - Показало: ('200', '30522')

`re.findall(r'\d+\.\d+', ryadok)`

**Передбачення:**  '172.16', '4.101', '1.1', '5.0', '605.1' - Вгадав - Показало: '172.16', '4.101', '1.1', '5.0', '605.1'

`re.sub(r'((\d+)/(\w+))/(\d+)', r'\4 \3 \2', '17/Mar/2026')`

**Передбачення:** 2026 Mar 17 - Вгадав - Показало: 2026 Mar 17
