# Mutiple Modules Project Template

- @author kazurayam
- @date Feb 2021

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [これは何か](#%E3%81%93%E3%82%8C%E3%81%AF%E4%BD%95%E3%81%8B)
- [IntelliJ IDEAで複数モジュールから成るプロジェクトを作った](#intellij-idea%E3%81%A7%E8%A4%87%E6%95%B0%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%81%8B%E3%82%89%E6%88%90%E3%82%8B%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%9F)
  - [pycliappサブプロジェクトの概要](#pycliapp%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E6%A6%82%E8%A6%81)
  - [pywebappサブプロジェクトの概要](#pywebapp%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E6%A6%82%E8%A6%81)
  - [pywebuitestサブプロジェクトの概要](#pywebuitest%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E6%A6%82%E8%A6%81)
- [pycliappサブプロジェクトの説明](#pycliapp%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E8%AA%AC%E6%98%8E)
- [pywebappサブプロジェクトの説明](#pywebapp%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E8%AA%AC%E6%98%8E)
- [pywebuitestサブプロジェクトの説明](#pywebuitest%E3%82%B5%E3%83%96%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E8%AA%AC%E6%98%8E)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## これは何か

ひとつのディレクトリのなかに複数のサブプロジェクトを格納したレポジトリです。今後わたしがいろいろ仕事をするためにいくつもレポジトリを作るだろう。そのたびに環境とツールを整備するのでは手間がかかりすぎる。できるかぎり努力してこのプロジェクトの環境とツールを整備したうえで、これを複写して新しいレポジトリの下敷きを作ろう。Git HubのTemplate Repository機能を利用しよう。

このレポジトリの最初のバージョンではPython言語によるサブプロジェクト３つを仕込むことにした。Pythonはプログラミング言語としてはとても習得しやすい洗練された言語だと思う。 ところがPython言語でプログラムを自作しようと手を動かし始めるとすぐに環境の問題に直面する。Python処理系それ自体のバージョンをどうするか、外部パッケージをどう管理するか、自作したコードをどうやってライブラリ化するか、開発作業をしたマシンとは別のマシンでどうやって動かすかといった問題だ。言語を学ぶのは楽でも開発環境を構築するノウハウを習得するのは決して易しくない。だから本プロジェクトにおいてわたしは自分のために、Pythonによる開発環境いかに構築すべきかの手本を準備しようと思う。

将来的にはサブプロジェクトの数は３つとかぎらないしPython言語だけとはかぎらない。サブプロジェクトをJavaやNodeで作ることもあるだろうな。

## IntelliJ IDEAで複数モジュールから成るプロジェクトを作った

わたしはJavaによる開発のため 統合開発環境 IntelliJ IDEA をずっと使ってきた。だからIDEAでPythonの開発もやることにした。IDEAでひとつの親プロジェクトのなかに複数のサブプロジェクトを持たせたかった。下記の記事を参考にした。

- [IntelliJ IDEAで複数モジュールのプロジェクトを作成する手順のメモ](https://qiita.com/rubytomato@github/items/e534e4f1187801b7e159)

下記のように３つのサブプロジェクトを作った

```
$ tree $ROOTPROJ
.
├── pycliapp
├── pywebapp
└── pywebuitest
```

>なお上記で `$ROOTPROJ` という記号を用いていた。これは本レポジトリをわたしのPCのローカルディスクにcloneすることによって作られたディレクトリ（たとえば `~/github/MultipleModulesProjectTemplate`）を表します。

3つのサブプロジェクトはどういう内容のプロジェクトか？

### pycliappサブプロジェクトの概要

このサブプロジェクトではcommandlineで実行するapplicationをPython言語で開発します。

1. 実行されるとコンソールに *Hello, World!* と表示するだけの
   シンプルなアプリケーションをPython言語で作ります
1. 標準的なPythonプロジェクトのディレクトリ構造を導入します
1. アプリケーションをユニットテストします。そのために[pytest](https://docs.pytest.org/en/stable/)を利用します
1. このサブプロジェクトに専用のPython仮想環境を作ります。[pipenv](https://pypi.org/project/pipenv/) を利用します
1. IntelliJ IDEAに適切な設定を加えます。この`pycliapp` プロジェクトの開発作業をIDEAのなかですべてできるようにします
1. 自作したPythonアプリケーションを [pip](https://pypi.org/project/pip/) でライブラリ化します。[PyPI](https://test.pypi.org/) に自分のためのアカウントを作って、PyPIにライブラリをアップロードして共有可能にします。
1. 自作したPythonアプリケーションを組み込んだ[Docker](https://www.docker.com/) イメージを作り、Dockerコンテナを立ち上げて自作アプリを動かします。[Docker Hub](https://hub.docker.com/) に自分のためのアカウントを作って、Docker Hubにイメージをアップロードして共有可能にします。


### pywebappサブプロジェクトの概要

このサブプロジェクトはWebサーバアプリケーションをPython言語で開発します。

1. フレームワーク [Flask](https://palletsprojects.com/p/flask/) の [チュートリアル](https://flask.palletsprojects.com/en/1.1.x/tutorial/) を隅々まで写経して、ちゃんと動作するWebアプリケーションを作ります。
1. チュートリアルのサンプルが動くDockerコンテナを自分のPCで立ち上げて、http://localhost:80/ でアクセスできるようにします。


### pywebuitestサブプロジェクトの概要

このサブプロジェクトはWebサーバアプリケーションのユーザー・インターフェースを自動化テストします。

1. `pywebapp`サブプロジェクトが構築したWebアプリを対象とします。
1. [Selenium](https://selenium-python.readthedocs.io/) を用いたPythonプログラムを開発してWebページをテストします。
1. Page Object Model のデザインを用いてテストコードを設計します。





## pycliappサブプロジェクトの説明

TODO

## pywebappサブプロジェクトの説明

TODO

## pywebuitestサブプロジェクトの説明


TODO