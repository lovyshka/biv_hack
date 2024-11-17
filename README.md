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


## Дерево каталогов

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

## Испытания
Испытания проходили на 
1) macbook pro m3 - время работы модели составило **4 минуты**
2) ASUS ROG Zephyrus G14 с процессором AMD Ryzen 5 4600HS  -  время работы модели составило **6 минуты**
3) macbook air m2 - время работы модели составило  **10 минут**(базовый слой был собран на другой архитектуре процессор, из-за чего просела скорость)
4) Был арендован сервер 4 ГБ оперативы, 2 ядра  Intel Xeon E5-2680 v2 (2) @ 2.793GHz  - время работы модели составило  **25 минут**