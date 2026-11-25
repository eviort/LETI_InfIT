from PIL import Image
from datetime import datetime


inp = input('Введите имя файла для обработки: ')

try:
    img = Image.open('Lab2_Media/data/input/' + inp).convert('RGB')
    wid, heg = img.size
    res = img.copy()
    src = img.load()
    cop = res.load()
    r_sum, g_sum, b_sum = 0, 0, 0

    for i in range(1, heg - 1):
        for j in range(1, wid - 1):
            rs, gs, bs = [], [], []
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    r, g, b = src[j + dj, i + di]
                    rs.append(r)
                    gs.append(g)
                    bs.append(b)
            rs.sort()
            gs.sort()
            bs.sort()
            cop[j, i] = (rs[4], gs[4], bs[4])

    for i in range(heg):
        for j in range(wid):
            r, g, b = cop[j, i]
            r_sum += r
            g_sum += g
            b_sum += b
    pxs = heg * wid
    r_avg = r_sum / pxs
    g_avg = g_sum / pxs
    b_avg = b_sum / pxs
    avg = (r_avg + g_avg + b_avg) / 3
    kr = avg / r_avg if r_avg != 0 else 1
    kg = avg / g_avg if g_avg != 0 else 1
    kb = avg / b_avg if b_avg != 0 else 1

    for i in range(heg):
        for j in range(wid):
            r, g, b = cop[j, i]
            r_new = min(255, int(r * kr))
            g_new = min(255, int(g * kg))
            b_new = min(255, int(b * kb))
            cop[j, i] = (r_new, g_new, b_new)
    res.save('Lab2_Media/data/output/result.jpg')
    ch = 'Успешно'

except PermissionError:
    print('Ошибка: Нет прав на чтение файла ' + inp + '. Обратитесь к администратору')
    ch = 'Ошибка доступа'
except FileNotFoundError:
    print('Ошибка: Файл не найден')
    ch = 'Файл не найден'

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('Lab2_Media/logs/history.txt', 'a', encoding='UTF-8') as log:
    log.write(date + ' Файл: Lab2_Media/data/input/' + inp + ' | Фильтр: Медианный фильтр и Баланс белого ("Серый мир") '
              + '| Статус: ' + ch + '\n')