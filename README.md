# ROSのTOPICを利用した足し算ノードのパッケージ

千葉工業大学 工学部 未来ロボティクス学科 3年 ロボットシステム学 課題2(ROSで何かを作る)

授業中のcount.pyとtwice.pyを改造しました。

scripts内のpub_cal.pyがパブリッシャ、sub_cal.pyがサブスクライバとなっている。

課題1で製作したデバイスドライバと組み合わせて使用することでLEDを点灯させることが出来ました。

使用方法

・https://github.com/IS4444/raspi_led_device_driverのデバイスドライバを使用する。

・roscoreする。

・pub_cal.pyとsub_cal.pyを別々のターミナルで起動させる。

・pub_cal.pyを起動させると足し算の問題が出力されて答えの入力を待ちます。

・答えを入力するとsub_cal.py側のターミナルに答え合わせの結果が出力されます。正解の場合は「Great!!」、不正解の場合は「Oh...」と出力されます。

・正解の場合GPIO22に挿したLEDが点灯し、不正解の場合はGPIO23に挿したLEDが点灯する。sub_cal.pyが終了した場合LEDが消灯します。

※pub_cal.pyにEnterキーか数字以外を入力するとノードが終了するようにしています。

