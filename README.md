# Japanese C Language (JCL) - VS Code Extension

日本語でCプログラミングができるVS Code拡張機能です！

## 🚀 特徴

- ✅ **シンタックスハイライト**: JCLコードが美しく色分け表示
- ✅ **F5実行**: ワンキーでJCLファイルを実行
- ✅ **ファイルアイコン**: .jcファイルに専用アイコン
- ✅ **言語認識**: VS CodeがJCLファイルを正しく認識

## 📝 使い方

### 1. インストール
VS Code Marketplaceから「Japanese C Language」をインストール

### 2. JCLファイルを作成
```jcl
#組み込む<標準入出力>
主関数() {
    表示("こんにちは、世界！改行);
    戻る 0;
}
```

### 3. 実行
- **F5キー**を押すだけで実行！

## 📖 使える日本語キーワード一覧

Japanese C Languageで使える日本語キーワードをすべて紹介します！

### 🔤 **データ型**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `整数型` | `int` | `整数型 数値 = 42;` |
| `実数型` | `double` | `実数型 価格 = 100.5;` |
| `文字型` | `char` | `文字型 文字 = 'A';` |
| `時刻型` | `time_t` | `時刻型 現在 = time(NULL);` |

### 🎛️ **制御構文**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `主関数` | `int main` | `主関数() { ... }` |
| `もし` | `if` | `もし(条件) { ... }` |
| `そうでなければ` | `else` | `そうでなければ { ... }` |
| `そうでなければもし` | `else if` | `そうでなければもし(条件) { ... }` |
| `繰り返し` | `for` | `繰り返し(i = 0; i < 10; i++) { ... }` |
| `間` | `while` | `間(条件) { ... }` |
| `選択` | `switch` | `選択(変数) { ... }` |
| `続行` | `continue` | `続行;` |
| `抜ける` | `break` | `抜ける;` |
| `戻る` | `return` | `戻る 0;` |

### 📺 **入出力関数**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `表示` | `printf` | `表示("こんにちは改行");` |
| `出力` | `printf` | `出力("数値: 整数改行", 42);` |
| `入力` | `scanf` | `入力("整数", &数値);` |
| `文字入力` | `getchar` | `文字入力();` |

### 💾 **ファイル操作**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `ファイル開く` | `fopen` | `ファイル開く("test.txt", "r");` |
| `ファイル閉じる` | `fclose` | `ファイル閉じる(ファイル);` |
| `ファイル入力` | `fscanf` | `ファイル入力(ファイル, "整数", &値);` |
| `ファイル出力` | `fprintf` | `ファイル出力(ファイル, "値: 整数改行", 42);` |
| `ファイルフォーマット入力` | `fscanf` | より詳細なファイル入力 |
| `ファイルフォーマット出力` | `fprintf` | より詳細なファイル出力 |
| `ファイル設定` | `fseek` | `ファイル設定(ファイル, 0, SEEK_SET);` |
| `ファイルフラッシュ` | `fflush` | `ファイルフラッシュ(stdout);` |

### 🧠 **メモリ管理**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `メモリ確保` | `malloc` | `メモリ確保(sizeof(int) * 10);` |
| `メモリ解放` | `free` | `メモリ解放(ポインタ);` |

### 📝 **文字列操作**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `文字列文字数` | `strlen` | `文字列文字数("Hello");` |
| `文字列複製` | `strcpy` | `文字列複製(コピー先, コピー元);` |
| `文字列結合` | `strcat` | `文字列結合(結合先, 結合元);` |

### ⏰ **時間関数**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `現在時刻` | `time` | `現在時刻(NULL);` |
| `時刻変換` | `ctime` | `時刻変換(&時刻);` |
| `ローカル時刻` | `localtime` | `ローカル時刻(&時刻);` |
| `時刻フォーマット` | `strftime` | `時刻フォーマット(文字列, サイズ, フォーマット, 時刻);` |

### 🎲 **乱数生成**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `乱数初期化` | `srand` | `乱数初期化(time(NULL));` |
| `乱数生成` | `rand` | `乱数生成() % 100;` |

### 🎯 **フォーマット指定子（文字列内で使用）**
| 日本語 | 変換後(C言語) | 使い方 |
|--------|---------------|--------|
| `整数` | `%d` | `"値: 整数"` → `"値: %d"` |
| `絶対整数` | `%u` | `"値: 絶対整数"` → `"値: %u"` |
| `整数16進` | `%x` | `"値: 整数16進"` → `"値: %x"` |
| `整数8進` | `%o` | `"値: 整数8進"` → `"値: %o"` |
| `h型整数` | `%hd` | `"値: h型整数"` → `"値: %hd"` |
| `絶対h型整数` | `%hu` | `"値: 絶対h型整数"` → `"値: %hu"` |
| `l型整数` | `%ld` | `"値: l型整数"` → `"値: %ld"` |
| `絶対l型整数` | `%lu` | `"値: 絶対l型整数"` → `"値: %lu"` |
| `l型整数16進` | `%lx` | `"値: l型整数16進"` → `"値: %lx"` |
| `l型整数8進` | `%lo` | `"値: l型整数8進"` → `"値: %lo"` |
| `実数` | `%f`(出力) / `%lf`(入力) | `"値: 実数"` → `"値: %f"` |
| `文字` | `%c` | `"文字: 文字"` → `"文字: %c"` |
| `文字列` | `%s` | `"名前: 文字列"` → `"名前: %s"` |
| `改行` | `\n` | `"Hello改行"` → `"Hello\n"` |

## 🔗 関連リポジトリ

このプロジェクトは、以下のリポジトリで構成されています：

- **[JCL-Extension](https://github.com/Konoa-1025/JCL-Extension)**: VS Code拡張機能（このリポジトリ）
- **[JCL-Engine](https://github.com/Konoa-1025/JCL-Engine)**: JCLトランスパイラエンジン

## 📋 要件

この拡張機能を使用するには、以下の要件を満たしている必要があります。

* **VS Code**: Visual Studio Codeがインストールされていること。
* **Python 3**: `runner.py` と `transpiler.py` の実行にPython 3が必要です。
* **GCC (または互換性のあるCコンパイラ)**: トランスパイルされたCコードをコンパイルするために、GCCなどのCコンパイラがシステムにインストールされ、パスが通っている必要があります。

## JCLコードの簡単な例

```jc
#組み込む<標準入出力> // C言語のstdio.hに相当

主関数() {
    出力("こんにちは、世界！改行"); // コンソールに出力
    整数型 i = 10;
    もし(i > 5) {
        出力("iは5より大きいです。改行");
    } そうでなければ {
        出力("iは5以下です。改行");
    }
    戻る 0;
}
```

## How to Use (使用方法)

1. VS Codeにこの拡張機能をインストールします。
2. VS CodeでJCLファイル（.jc 拡張子のファイル）を開きます。
3. F5キーを押します。
4. 自動的にJCLコードがCにトランスパイルされ、コンパイル、実行されます。結果は新しいターミナルウィンドウに表示されます。

## 🤖 自動生成コードについて

JCLで作成されたプログラムをCにトランスパイルすると、コード中に**「JCLによって自動生成されました」**というコメントが含まれることがあります。

### なぜこの表記があるのか？

これらのコメントは、JCLトランスパイラが自動的に追加する機能コードに付けられています：

1. **文字化け防止**: 
   - `printf()` 関数の後に自動的に `fflush(stdout);` を追加
   - 日本語出力時の文字化けを防止

2. **日本語環境設定**:
   - `main()` 関数の開始時に `setlocale(LC_ALL, "ja_JP.UTF-8");` を自動挿入
   - 日本語文字の正しい表示を保証

3. **必要なヘッダファイル**:
   - `#include <locale.h>` を自動的に追加
   - ロケール設定に必要なライブラリを自動インクルード

これらの自動生成コードにより、JCLユーザーは日本語の処理について詳しく知らなくても、正しく日本語が表示されるプログラムを作成できます。

c言語のみで開発する場合は不必要です。

## Known Issues (既知の問題)

現時点では特定の既知の問題はありませんが、もし問題を発見した場合は、GitHubリポジトリのIssuesページにご報告ください。

## Release Notes (リリースノート)

### 0.0.1 (Initial Release)

- JapaneseC言語のシンタックスハイライトを追加しました。
- `.jc`, `.c`, `.out` ファイルのカスタムアイコンを追加しました。
- F5キーでのJCLコードのトランスパイル、コンパイル、実行機能を追加しました。

## License (ライセンス)

この拡張機能は、以下のMITライセンスの下で公開されています。

```
MIT License

Copyright (c) 2025 Norifumi Kondo(Studio.Δ). All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

著作権表示:  
Copyright (c) 2025 Norifumi Kondo(Studio.Δ). All rights reserved.

Enjoy!

# jc-lang Project 2025

**jc言語**は、日本語で書けるC言語ベースの教育用プログラミング言語です。  
初心者でもプログラムの構造を直感的に理解できるように設計されています。

この言語は、**U-22プログラミング・コンテスト**への応募作品として開発されています。
