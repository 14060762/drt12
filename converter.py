def run_converter():

    print("\n--- Инженерный калькулятор систем счисления ---")
    print("Доступные системы: dec (десятичная), bin (двоичная), hex (шестнадцатеричная)")
    
   
    mode = input("Выберите исходную систему (dec, bin, hex): ").strip().lower()
  
    number_str = input("Введите число для конвертации: ").strip()

    if mode == 'dec':
        try:
            dec_number = int(number_str)
            print(f"Входное (DEC): {dec_number}")
            # bin() добавляет 0b, срезаем первые 2 символа через [2:]
            print(f"Двоичное (BIN): {bin(dec_number)[2:]}") 
            # hex() добавляет 0x, срезаем и делаем буквы заглавными
            print(f"Шестнадцатеричное (HEX): {hex(dec_number)[2:].upper()}") 
        except ValueError:
            print("Ошибка: введено неверное десятичное число.")

    elif mode == 'bin':
        try:
            # int(..., 2) переводит из двоичной строки
            dec_number = int(number_str, 2)
            print(f"Входное (BIN): {number_str}")
            print(f"Десятичное (DEC): {dec_number}")
            print(f"Шестнадцатеричное (HEX): {hex(dec_number)[2:].upper()}")
        except ValueError:
            print("Ошибка: введено неверное двоичное число (нужны только 0 и 1).")

    elif mode == 'hex':
        try:
            # int(..., 16) переводит из 16-ричной строки
            dec_number = int(number_str, 16)
            print(f"Входное (HEX): {number_str}")
            print(f"Десятичное (DEC): {dec_number}")
            print(f"Двоичное (BIN): {bin(dec_number)[2:]}")
        except ValueError:
            print("Ошибка: введено неверное 16-ричное число (0-9, A-F).")

    else:
        print("Ошибка: выбран неверный режим. Напишите dec, bin или hex.")

# Запуск программы
if __name__ == "__main__":
    run_converter()