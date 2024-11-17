# HACKATON_2024_BIV

## Быстрый старт

1) Склонируйте данный репозиторий

``` bash
git clone https://github.com/lovyshka/biv_hack.git
```

2) Перейдите в корень репозитория

``` bash
cd biv_hack
```

3) Замените файл data/payments_main.tsv, на ваш файл **с таким же названием**.


4) Собери новый docker образ 

``` bash
docker build -t strog_kabans_model_image . 
```

5) Запустите контейнер

``` bash
docker run -d --name strog_kabans_model_cont -v ./data:/tmp/data strog_kabans_model_image
```


## Обзор

```
.
├── Claustering_data.ipynb - тетрадка в которй велась основная работы 
├── data
|   |   output.csv         - ЭТОТ ФАЙЛ ПОЯВИТСЯ ПОСЛЕ РАБОТЫ КОНТЕЙНЕРА
│   └── payments_main.tsv  - ВОТ ЭТОТ ФАЙЛ НЕОБХОДИМО ЗАМЕНИТЬ НА ВАШ
├── docker-compose.yml     - файл для запуска контейнера
├── Dockerfile             - файл для сборки нового образа
├── model
│   ├── main.py            - упакованный в .py код для разметки
│   ├── model_weghts       - веса модели, которая получилась в тетрадке
│   └── requirements.txt   - файлик с зависимостями
└── README.md              - мы здесь)

2 directories, 9 files
```