# automatic-health-check-sheet

## feature

健康チェックシートの
- 起床時刻 
- 就寝時刻
- 朝の体温
をランダムで出力します

デフォルトで以下の範囲で出力

||範囲|
|----|----|
|起床時刻|6:00~9:00|
|就寝時刻|20:00~24:00|
|朝の体温|36'0~37'0|
## requirements
python==3.8  
pandas==1.03

## usage
`main.py`を実行
### デフォルト値を変更
#### 体温
`main.py`の`body-temperature`を変更
```python
body_temperature = {
    "min": 36.0,
    "max": 37.0
    }
```
#### 日付
`main.py`の`date`を`'YYYY-mm-dd'`形式で変更
```python
date = {
    "start": '2020-06-11',#format: 'YYYY-mm-dd'
    "end": '2020-06-24', #format: 'YYYY-mm-dd'
    }
```
