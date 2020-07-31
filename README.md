# 2007_DIY_Live



## Requirements
- Ableton Live 10.1.15
- Max 8.1.5
- Download [this repo](https://github.com/hana/ht.min) to `Max 8/packages`

## ファイル構成
`Ableton` フォルダ
- 演者が使ったAbleton Liveのプロジェクト + M4Lデバイス

`Hub` フォルダ
- 遠隔地にいる演者の演奏データを共有するためのサーバーで走っているnode.jsスクリプト。

`RPi` フォルダ
- Raspberry Pi上で実行され、サーボとNeoPixelを制御する

## 初期化
### サーバーの起動
以下はサーバー上で実行
1. `Hub`フォルダ内の`package.js`を基に依存ファイルをnpmなどでインストール。
2. `Hub/main.js`の`Listen_Port`を指定する。
3. `main.js`を実行する。

### Max for Liveの設定
2. `Ableton/performance Project/src/SocketHub/socket.js`の`Host_Address`を、上記のサーバー, ポートに指定。

### Node for Maxで使うライブラリのインストール
1. Masterトラックにある`SocketHub`というデバイスの`Stop`ボタンを押す。
2. その右にあるDebug Windowの`Open`ボタンを押す。
3. 新たなウインドウが開いたら`Install`ボタンを押す。
4. `Success`が出たらウインドウを閉じ、SocketHubの`Start`ボタンを押す。
