from typing import Dict, Tuple

def read_file(file_name: str) -> Tuple[Dict[str, str], int]:
    """
    Читает файл и возвращает словарь пар слов и общее количество строк.
    """
    pairs: Dict[str, str] = {}
    total_lines = 0

    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                total_lines += 1
                line = line.strip()
                if not line:
                    continue

                # Разделяем строку на пару ключ-значение
                parts = line.split(" - ")
                if len(parts) != 2:
                    continue

                key, value = parts
                key, value = key.strip(), value.strip()

                # Добавляем пару в словарь
                pairs[key] = value

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
        return {}, 0

    return pairs, total_lines


def write_to_file(pairs: Dict[str, str], output_file: str = "output.txt") -> None:
    """
    Записывает пары ключ-значение в выходной файл.
    """
    try:
        with open(output_file, 'w', encoding="utf-8") as file:
            for key, value in pairs.items():
                file.write(f"{key} - {value}\n")
    except IOError:
        print(f"Ошибка: Не удалось записать в файл '{output_file}'.")


def main() -> None:
    """
    Основная функция программы.
    """
    file_path = input("Введите путь к файлу: ").strip().replace("\"", "")
    pairs, total_lines = read_file(file_path)

    if not pairs:
        print("Файл пуст или содержит некорректные данные.")
        return

    write_to_file(pairs)
    print("Содержимое словаря:")
    for key, value in pairs.items():
        print(f"{key} - {value}")

    print(f"Было строк: {total_lines}")
    print(f"Стало уникальных пар: {len(pairs)}")


if __name__ == '__main__':
    main()