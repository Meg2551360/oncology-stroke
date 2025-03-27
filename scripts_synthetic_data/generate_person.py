import os
import random
import argparse
import numpy as np
import pandas as pd

from scipy.stats import norm, bernoulli
from src.utils.config import import_config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config',
        type=str,
        help='Path to generator config'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = import_config(args.config)
    random.seed(config.SEED)
    np.random.seed(config.SEED)

    # Start generate
    columns = {}
    num_samples = config.NUM_SAMPLES

    columns['№ пациента'] = ['Пациент ' + str(i) for i in range(num_samples)]
    columns['Возраст'] = [int(age) for age in
                          norm.rvs(loc=config.MU_AGE, scale=config.SIGMA_AGE, size=num_samples).tolist()]
    columns['Пол'] = ['мужской' if i == 1 else 'женский' for i in
                      bernoulli.rvs(p=config.P_GENDER, size=num_samples).tolist()]
    columns['Тип инсульта'] = ['Нет' for _ in range(num_samples)]
    columns['Атеротромботический'] = ['Нет' for _ in range(num_samples)]
    columns['Кардиоэмболический'] = ['Нет' for _ in range(num_samples)]
    columns['Криптогенный'] = ['Нет' for _ in range(num_samples)]
    columns['Лакунарный'] = ['Нет' for _ in range(num_samples)]
    columns['Левая СМА'] = ['Нет' for _ in range(num_samples)]
    columns['Правая СМА'] = ['Нет' for _ in range(num_samples)]
    columns['ВББ'] = ['Нет' for _ in range(num_samples)]
    columns['Степень артериальной гипертензии'] = [0 for _ in range(num_samples)]
    columns['Артериальное давление'] = [str(str(int(s)) + '/' + str(int(d))) for s, d in
                                        zip(norm.rvs(loc=config.MU_SYSTOLIC,
                                                     scale=config.SIGMA_SYSTOLIC,
                                                     size=num_samples),
                                            norm.rvs(loc=config.MU_DIASTOLIC,
                                                     scale=config.SIGMA_DIASTOLIC,
                                                     size=num_samples))]
    columns['Артериальная гипертензия'] = ['да' if i == 1 else 'нет' for i in
                                           bernoulli.rvs(p=config.P_ARTERIAL_HYPERTENSION,
                                                         size=num_samples).tolist()]
    columns['Фибрилляции предсердий'] = ['да' if i == 1 else 'нет' for i in
                                         bernoulli.rvs(p=config.P_ARTERIAL_FIBRILLATION,
                                                       size=num_samples).tolist()]
    columns['ИМТ'] = norm.rvs(loc=config.MU_BMI, scale=config.SIGMA_BMI, size=num_samples).tolist()
    columns['Сахарный диабет'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=config.P_DIABETES,
                                                                                   size=num_samples).tolist()]
    columns['Инфаркта миокарда'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=config.P_MYOCARDIAL_INFARCT,
                                                                                     size=num_samples).tolist()]
    columns['ИБС'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=config.P_CARDIAC_ISCHEMIA,
                                                                       size=num_samples).tolist()]
    columns['Гипертрофия миокарда'] = ['да' if i == 1 else 'нет' for i in
                                       bernoulli.rvs(p=config.P_MYOCARDIAL_HYPYERTROPHY,
                                                     size=num_samples).tolist()]
    columns['ХСН'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=config.P_CHRONIC_HEART_FAILURE,
                                                                       size=num_samples).tolist()]
    columns['Атеросклероз коронарных артерий'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=0,
                                                                                                   size=num_samples).tolist()]
    columns['Атеросклероз брахиоцефальных артерий'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=0,
                                                                                                        size=num_samples).tolist()]
    columns['Атеросклероз сосудов головного мозга'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=0,
                                                                                                        size=num_samples).tolist()]
    columns['Атеросклероз аорты'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=0,
                                                                                      size=num_samples).tolist()]
    columns['Наличие ТИА/ОНМК'] = ['да' if i == 1 else 'нет' for i in bernoulli.rvs(p=0,
                                                                                    size=num_samples).tolist()]
    columns['Курение'] = ['Да' if i == 1 else 'Нет' for i in
                          bernoulli.rvs(p=config.P_SMOKING, size=num_samples).tolist()]
    columns['Алкоголь'] = ['Да' if i == 1 else 'Нет' for i in
                           bernoulli.rvs(p=config.P_DRINK, size=num_samples).tolist()]
    columns['ХОБЛ'] = ['Нет' for _ in range(num_samples)]
    columns['Пневмония'] = ['Нет' for _ in range(num_samples)]
    columns['Дыхательная недостаточность'] = ['Нет' for _ in range(num_samples)]
    columns['ХБП'] = ['Нет' for _ in range(num_samples)]
    columns['Анемия'] = ['Нет' for _ in range(num_samples)]
    columns['Тромбоцитопения'] = ['Нет' for _ in range(num_samples)]
    columns['Количество дней'] = [0 for _ in range(num_samples)]
    columns['Онкологический диагноз у пациента'] = ['Нет' for _ in range(num_samples)]
    columns['Холестерин'] = [round(i, 2) for i in norm.rvs(loc=config.MU_CHOLESTEROL, scale=config.SIGMA_CHOLESTEROL,
                                                           size=num_samples).tolist()]
    columns['ЛПВП'] = [round(i, 2) for i in norm.rvs(loc=config.MU_HIGH_DENSITY_LIPOPROTEINS,
                                                     scale=config.SIGMA_HIGH_DENSITY_LIPOPROTEINS,
                                                     size=num_samples).tolist()]
    columns['ЛПНП'] = [round(i, 2) for i in norm.rvs(loc=3.1, scale=1.0, size=num_samples).tolist()]
    columns['Индекс атерогенности'] = [round(i, 2) for i in norm.rvs(loc=2.5, scale=0.8, size=num_samples).tolist()]
    columns['Триглицериды'] = [round(i, 2) for i in norm.rvs(loc=1.1, scale=0.4, size=num_samples).tolist()]
    columns['Гемоглобин'] = [round(i, 2) for i in norm.rvs(loc=140, scale=46.7, size=num_samples).tolist()]
    columns['Гематокрит'] =[round(i, 2) for i in  norm.rvs(loc=42, scale=14, size=num_samples).tolist()]
    columns['Лейкоциты'] = [round(i, 2) for i in norm.rvs(loc=6.5, scale=2.2, size=num_samples).tolist()]
    columns['Эритроциты'] = [round(i, 2) for i in norm.rvs(loc=4.5, scale=1.5, size=num_samples).tolist()]
    columns['MCV'] = [round(i, 2) for i in norm.rvs(loc=90, scale=30, size=num_samples).tolist()]
    columns['RDW_э'] = [round(i, 2) for i in norm.rvs(loc=45.5, scale=15.2, size=num_samples).tolist()]
    columns['Тромбоциты'] = [round(i, 2) for i in norm.rvs(loc=265, scale=88.3, size=num_samples).tolist()]
    columns['RDW_т'] = [round(i, 2) for i in norm.rvs(loc=13, scale=4.3, size=num_samples).tolist()]
    columns['Коэффициент больших тромбоцитов'] = [round(i, 2) for i in norm.rvs(loc=28, scale=9.3, size=num_samples).tolist()]
    columns['МНО'] = [round(i, 2) for i in norm.rvs(loc=1.05, scale=0.35, size=num_samples).tolist()]
    columns['АЧТВ'] = [round(i, 2) for i in norm.rvs(loc=33, scale=11, size=num_samples).tolist()]
    columns['ПТВ'] = [round(i, 2) for i in norm.rvs(loc=14.5, scale=4.8, size=num_samples).tolist()]
    columns['Больной'] = ['Нет' for _ in range(num_samples)]

    df = pd.DataFrame(columns)
    df.to_excel('data/сгенерированные.xlsx', index=False)


if __name__ == '__main__':
    main()
