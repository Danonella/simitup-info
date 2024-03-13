def process_file(filename):
    with open(filename) as f:
        n = int(f.readline())
        summ = 0
        array = []

        for i in range(n):
            x = int(f.readline())
            array.append(x)
            summ += x

        # Сколько не хвататет убрать до ровного деления
        remainder = summ % 89

        summ1 = 0
        k1 = 0

        # идем сверху вниз, пока не получим сумму кратную 89
        for i in range(n):
            summ1 += array[i]
            k1 += 1
            if summ1 % 89 == remainder:
                break

        summ2 = 0
        k2 = 0

        # идем снизу вверх, пока не получим сумму кратную 89
        for i in range(n - 1, -1, -1):
            summ2 += array[i]
            k2 += 1
            if summ2 % 89 == remainder:
                break

        # выбираем наименьшую сумму
        if summ1 < summ2:
            main_summ = summ1
            count = k1
        else:
            main_summ = summ2
            count = k2

        if summ1 == summ2:
            count = max(k1, k2)

        summ3_1 = 0
        k3_1 = 0

        # идем одновременно снизу и сверху, начиная сверху
        for i in range(n):
            if summ3_1 > main_summ:
                break
            summ3_1 += array[i]
            k3_1 += 1

            k3_2 = 0
            summ3_2 = 0

            j = n - 1
            while j >= 0:
                summ3_2 += array[j]
                k3_2 += 1
                if (summ3_1 + summ3_2) % 89 == remainder:
                    if (summ3_1 + summ3_2) < main_summ:
                        main_summ = summ3_1 + summ3_2
                        count = k3_1 + k3_2

                    if summ3_1 + summ3_2 == main_summ:
                        count = max(count, k3_1 + k3_2)

                    break
                j -= 1

        summ4_1 = 0
        k4_1 = 0

        # идем одновременно сверху и снизу, начиная снизу
        for i in range(n - 1, -1, -1):
            if summ4_1 > main_summ:
                break
            summ4_1 += array[i]
            k4_1 += 1

            k4_2 = 0
            summ4_2 = 0

            j = 0
            while j < n:
                summ4_2 += array[j]
                k4_2 += 1
                if (summ4_1 + summ4_2) % 89 == remainder:
                    if (summ4_1 + summ4_2) < main_summ:
                        main_summ = summ4_1 + summ4_2
                        count = k4_1 + k4_2

                    if summ4_1 + summ4_2 == main_summ:
                        count = max(count, k4_1 + k4_2)

                    break
                j += 1

        if remainder == 0:
            return n
        else:
            return n - count


#Запуск функции и печать ответа
print(process_file('27_A.txt'))
print(process_file('27_B.txt'))
