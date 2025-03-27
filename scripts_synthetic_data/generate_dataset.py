import pandas as pd
import argparse

DROP_COLUMNS = ['№ пациента', 'Артериальное давление', 'Количество дней', 'Тип инсульта', 'Атеротромботический',
                'Кардиоэмболический', 'Криптогенный', 'Лакунарный', 'Левая СМА', 'Правая СМА', 'ВББ',
                'Онкологический диагноз у пациента', 'Степень артериальной гипертензии']


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file1',
        type=str,
        help='Path to first file'
    )
    parser.add_argument(
        'file2',
        type=str,
        help='Path to second file'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    df1 = pd.read_excel(args.file1)
    df2 = pd.read_excel(args.file2)
    # Concat and shuffle
    df = pd.concat([df1, df2], axis=0).sample(frac=1, random_state=42)
    # Split Артериальное давление column into 'верхнее', 'нижнее' columns
    df[['верхнее', 'нижнее']] = df['Артериальное давление'].str.split('/', expand=True).map(lambda x: int(x))

    # Drop columns
    df.drop(DROP_COLUMNS,
            axis=1,
            inplace=True)
    # Clear string columns
    object_columns = df.select_dtypes(include=['object']).columns
    for column in object_columns:
        df[column] = df[column].apply(lambda x: x.lower().replace(' ', ''))
    # да or нет to bool
    df.replace('да', True, inplace=True)
    df.replace('нет', False, inplace=True)

    # Save file
    df.to_excel('data/dataset.xlsx', index=False)


if __name__ == '__main__':
    main()
