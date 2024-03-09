# CompressedFrame
класс для передачи DataFrame в Apache AirFlow между тасками через xcom

Принцип работы заключается в сжатии датафрейм и передачи json объекта, содержащего полезные данные и hex строку с байтами сжатого архива.

В чем разница между передачей датафрейм в виде стандартного json и данного решения:
- передача данных в сжатом виде позволит вместить в xcom гораздо больше данных
- датафрейм забирается в другом таске в том же виде, в котором был передан, т.е. не нужно делать дополнительные преобразования для колонок с типом данных Date/Datetime

пример использования:

```python
from polars import DataFrame

from compressed_frame import CompressedFrame


df = DataFrame({"a": [1, 2, 3], "b": [1.0, 2.1, 3.2]})

comp_df = CompressedFrame(df) # можно передать в класс pandas.DataFrame, polars.DataFrame,
                              # класс compressed_frame.struct.CompactFrame
                              # либо Tuple/List объект, полученный из xcom
print(comp_df)                # посмотреть вывод объекта
print(comp_df.push)           # выгрузить Tuple/List объект в xcom
print(comp_df.pull)           # преобразовать в исходный DataFrame
```

вывод скрипта в консоль:

```bash
CompactFrame for polars DataFrame    
---------------------------------    
Columns:             ['a', 'b']      
Data types:          [Int64, Float64]
Columns numbers:     2
DataFrame count:     3
Size as pickle dump: 795 bytes       
Compressed size:     277 bytes       
Copmressed ratio:    65.16%
CRC32:               d12d315d        
('polars_frame', "['a', 'b']", '[Int64, Float64]', 2, 3, 795, 277, 65.16, 'd12d315d', '78da6b60992ac0cc00063d6205f9398945c57a29892589694589b9a97a60724a0fa70b50c40dcc9e3c45b3714aec148d1e11a8e2e2d4a2cc541835a5872d18c200ab738a606460f80f041540e35980f813902d0266032518b818b8193880240bc30fa0380f5084030861b220f56f80e216405a0188258098918981418041082827c0200856cb0376fa17a03a07903cd80c4ea03c07989dc800b1bf03c93c07886f1920ee60069a200c369307c87b06948786068303540d047001d92c4035020c4c0cb88104121b643f3316358c501a660e33036900e41f103d2529831d14c601d0302ea0208c0d90c398197b18ff02aa636260034288dea44118b610f0c1feec1910607098351304381d480fdbd4243d008afc8177')  
shape: (3, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ f64 │
╞═════╪═════╡
│ 1   ┆ 1.0 │
│ 2   ┆ 2.1 │
│ 3   ┆ 3.2 │
└─────┴─────┘
```
