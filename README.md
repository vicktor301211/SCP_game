# SCP_game
### 1. Описание проекта
#### Данный проект представляет собой двухмерную игру на тематику scp, действия которой происходят в Зоне 19.
### 2. Сюжет
#### Вы играете за сотрудника Фонда на ваш выбор. В Зоне 19 происходит нарушение условий содержания scp - объектов. Ваша задача - выжить, и либо нейтрализовать угрозы, либо эвакуироваться из комплекса.
### 3. Персонажи
#### Вы можете играть за любого из сотрудников Фонда либо за их врагов - группировки Повстанцы Хаоса. Всего вы можете играть за 5 фракций, каждая из которых принадлежит к одному из двух классов. После эвакуации на ваш выбор вы можете продолжить играть за персонажа той же фракции, либо же просто завершить игру, эвакуировавшись.
## Внимание! Далее представлена информация только для разработчиков! Не читайте (Вы всё равно вряд ли что-либо поймёте)
### 4. Классы
#### В игре есть три класса(хитбокс не учитываем), два из которых игровые, а третий - scp. Главный аргумент класса - принадлежность к фракции. Названия классов: Фонд, Повстанцы, SCP. Фракции (для игровых классов): Д-Класс(Повстанцы), МОГ(Фонд), Учёные(Фонд), Охрана(Фонд), Повстанцы Хаоса(Повстанцы). Для SCP пропишу я сам. Главная фишка игры: выбор фракции.
### 5. Роли (Фракции)
### 5.1 Д-Класс
#### Класс D присваивается расходному персоналу, используемому для работ с крайне опасными аномалиями. Сотрудники класса D обычно набираются из заключённых во всех странах мира, предпочтение отдаётся осуждённым за насильственные преступления и особенно приговорённым к смертной казни. Набранные сотрудники перевозятся в учреждения Фонда под достоверным предлогом. Сотрудников класса D необходимо регулярно подвергать обязательным психиатрическим обследованиями, а в конце месяца - или обрабатывать амнезиаком класса B (или более сильным), или ликвидировать, на усмотрение местной службой безопасности или медицинской службы. В случае возникновения в учреждении катастрофического события все местные сотрудники класса D подлежат немедленному уничтожению, если только местная служба безопасности не примет иное решение.
#### Как вы поняли, у Д-Класса (далее - Дэшки или Дшки) незавидная судьба. Соответственно, если игрок играет за Дэшку, он подлежит ЛИКВИДАЦИИ. Уровень допуска - 0. Задача - побег и мщение
### 5.2 Сотрудники службы безопасности
#### Служба безопасности учреждений (часто называемая просто "охраной") занимается обеспечением физической и информационной безопасности проектов, операций и персонала Фонда. Сотрудники службы безопасности набираются главным образом из военных, сотрудников правоохранительных органов и персонала исправительных учреждений. Они владеют многими видами оружия, а также обучены действовать в целом ряде чрезвычайных ситуаций, включая как нарушения условий содержания, так и враждебные действия. Сотрудники службы безопасности также ответственны за информационную безопасность, в частности, за защиту компьютерных систем учреждения от вторжения извне, а также за сохранность физических копий секретной документации. Кроме того, сотрудники службы безопасности часто оказываются первой линией обороны в случае враждебного вторжения в учреждение Фонда.
#### Исходя из статьи, охрана должна быть вооружена как минимум пистолетами-пулемётами. Уровень допуска - 2-4(Зависит от роли). Задача - помощь МОГ
### 5.3 Научные сотрудники
#### Научные сотрудники отвечают за исследовательскую деятельность Фонда, они набираются из самых одарённых и квалифицированных учёных по всему миру. Среди них есть специалисты во всех возможных областях знаний, начиная с химии и ботаники и заканчивая такими малоизвестными и узкоспециализированными областями, как теоретическая физика и ксенобиология. Целью исследовательских проектов Фонда является лучшее понимание необъяснённых аномалий и принципов их действия.
#### "Учёные - в г**не мочёные!" - рандомный чел из Интернета
#### Научники должны иметь при себе ключ-карту 2 - 4 уровня доступа и вагон знаний в голове. Их задача эвакуироваться и присоединиться к МОГ
### 5.4 Оперативники МОГ
#### Мобильные оперативные группы - это специализированные подразделения, собранные из агентов-ветеранов самых разных учреждений Фонда и используемые в случаях специфических угроз. Их состав крайне различен - мобильная опергруппа может состоять как из полевых исследователей, специализирующихся в определённом типе аномалий, так и представлять собой тяжеловооружённый отряд, обученный справляться с конкретным видом враждебных аномальных существ.
#### Задача этих парней - сдерживание аномальных существ в комплексе. Имеют отличное вооружение и оборудование. Уровень доступа - 3 или 4
### 5.5 Повстанцы Хаоса
#### Повстанцы Хаоса — объединение, отделившееся от Фонда. Оно возникло в 1924 г., когда одно из подразделений самовольно покинуло свой участок, взяв с собой несколько крайне полезных SCP-объектов. С тех пор Повстанцы превратились в крупного игрока на мировой сцене. Они используют SCP-объекты, находящиеся в их распоряжении, в интересах личной выгоды и для укрепления глобальной политической поддержки. Повстанцы имеют дело не только с SCP-объектами, но также занимаются поставками оружия и сбором информации. https://scpfoundation.net/chaos-insurgency-hub (инфа тут)
#### Сие граждане должны помочь Дэшкам выбраться из комплекса и захватить пару объектов. Уровень допуска - [ДАННЫЕ УДАЛЕНЫ]
### 6. Смерть
#### Ну что тут сказать... Просто смерть. Даже добавить нечего
### 7. Распределение обязанностей. Здесь будут все обязанности каждого члена команды
#### 03.12.24
#### Тимур - создать класс SCP - 173. 173 должен двигаться, когда игрок моргает. Сам 173 должен выглядеть как красный квадрат(пока)
#### Арсений - создать класс SCP - 106. 106 должен двигаться за игроком. Выглядит как серый квадрат
#### Саша - Создать класс Insurgency. В него входят Повстанцы Хаоса и Дэшки. Цвет - для дэшек оранжевый, для повстанцев - зелёный
#### Я создаю класс Foundation. Что в нём будет скажу потом
### Вся информация была взята с официального сайта scp foundation. Ссылка: https://scpfoundation.net/
