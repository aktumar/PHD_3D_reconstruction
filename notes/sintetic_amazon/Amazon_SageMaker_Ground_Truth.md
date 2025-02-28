```
Amazon SageMaker Ground Truth
```



<a name="1" />

- У некоторых роботов есть задачи, которые можно легко определить
общим языком программирования. Это смесь входов, выходов, условий, циклов и логики.
Но чем более **автономным становится робот**, тем больше вероятность того, что он будет полагаться на ту или иную форму **машинного обучения**.

- Одним из наиболее значительных **достижений в области робототехники** за последние пять лет является внедрение передовых систем восприятия.
которые позволяют роботам **видеть и понимать мир** тонкими способами.
Эти модели восприятия управляются приложениями машинного обучения. 

- **Люди обладают замечательной способностью схватывать и распознавать объекты** в динамичной среде повседневной жизни.
Чтобы роботы помогали нам, мы должны иметь возможность подражать этим способностям.
Машинное обучение — ключ к этому.

- Многие **прорывы в области машинного обучения** исходят от таких исследовательских институтов, как Колумбийский, Массачусетский технологический институт и Калифорнийский университет в Лос-Анджелесе.

- У нас также есть большое и растущее **сообщество ученых**, которые активно исследуют и **публикуют инновационные статьи**,
более 500 публикаций в 2021 году. Вместе мы открываем новые пути и возможности
для студентов и исследователей. Amazon — это место, где исследования встречаются с реальностью.

- Этот вид робототехники в Амазон объединяет многие дисциплины,
включая **компьютерное зрение, планирование пути, локализацию и картирование**.

- Многие из наших клиентов используют **машинное обучение AWS** для создания роботов интересными способами.
**Boston Dynamics** — отличный тому пример. Они не только строят роботов, которые могут
ходить по промышленным объектам, они также могут использовать **тепловые датчики для обнаружения дефектов** и оповещения обслуживающего персонала о проблемах
пока они не превратились в большие проблемы. 

- Модели машинного обучения лучше всего учатся, когда им предоставляется множество простых изображений.
Тем не менее, часто бывает **трудно найти достаточно обучающих данных**, чтобы зафиксировать огромное разнообразие и пограничные случаи.
И даже если вы получите эти изображения реального мира, представляющие все возможные сценарии,
процесс их точного комментирования может занять месяцы.
Конечно, можно обучить модель машинного обучения всего на нескольких сотнях изображений.
Но если вам нужно построить робота вроде Робина, способного точно распознавать и подбирать предметы,
для этого ваша модель машинного обучения должна быть обучена на многих тысячах образцов изображений.
Так что же делать, если у вас просто нет необходимого количества образцов изображений?
Ответ: **синтетические данные**. 

- Генерация синтетических данных для **Amazon SageMaker Ground Truth**
— это функция, которая позволяет специалистам по данным генерировать данные изображения, чтобы они могли обучать более точные модели машинного обучения.
Генерация синтетических данных позволяет клиентам получать высококачественные и точные обучающие данные в масштабе всего за несколько недель.
И это дешевле, чем традиционные механизмы сбора данных, что экономит время и деньги.

- В качестве примера возьмем **Amazon Box**. Чтобы начать создание синтетических обучающих изображений,
  - вы предоставляете **3D модель объекта**, возможно модель вашего продукта разных форм и размеров упаковки.
  _Если у вас нет готовых 3D-изображений, наша команда состоит из узкоспециализированных технических художников.
  которые могут помочь вам создать их._ 
  - Вы также предоставляете **ряд сцен**, которые представляют окружающую среду.
  в который будет помещен объект. 

- Amazon SageMaker Ground Truth помогает создать как можно больше синтетических фотореалистичных изображений из трехмерных виртуальных сред,
которые представляют **сценарии реального мира, включая физические силы и условия, такие как гравитация и освещение**.

- Каждая фотография создается с помощью вашей 3D-модели или объекта, **имитирующего вашу среду и конфигурацию вашей камеры**.
Если робот, которого вы строите, использует камеру 720p,
вы хотите, чтобы синтезированные данные также были в этом разрешении. Конечная цель — обучить точные модели машинного обучения.
Таким образом, все должно соответствовать тому, что ваш сенсор будет снимать в процессе производства, от разрешения камеры до освещения.
Вы настроите свойства и варианты, которые определяют каждый потенциальный сценарий, такие как поза объекта, размер,
количество, вариации поверхности и освещение.
Затем вы указываете количество изображений для создания, а также желаемые типы меток,
такие как двумерные ограничивающие рамки, сегментация экземпляров и элементы управления.
**В течение нескольких часов сервис сгенерирует тысячи разнообразных изображений с автоматической маркировкой**